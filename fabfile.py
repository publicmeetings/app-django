from datetime import datetime
from fabric.api import cd, env, local, run, sudo
from fabric.utils import abort
from fabric.context_managers import settings

DJANGO_ENV = None

CONFIG = {}
CONFIG['APACHE_CONF_DIR'] = '/etc/apache2'
CONFIG['REPO_SRV'] = 'git@github.com'
CONFIG['REPO_OWNER'] = 'publicmeetings'
CONFIG['REPO_NAME'] = 'app-django'
CONFIG['REMOTE_SOURCE_REPO'] = '%(REPO_SRV)s:%(REPO_OWNER)s/%(REPO_NAME)s.git' % CONFIG


def _config():
    global DJANGO_ENV
    global CONFIG

    CONFIG['DJANGO_ENV'] = DJANGO_ENV
    CONFIG['SRV_DIR'] = '/srv/' + CONFIG['REPO_NAME']
    CONFIG['SRV_SOURCE_REPO'] = '~/%(DJANGO_ENV)s/%(REPO_NAME)s' % CONFIG
    CONFIG['HTTP_CONF_FILE'] = 'etc/http/%(REPO_NAME)s.conf' % CONFIG


def prod():
    global DJANGO_ENV
    global CONFIG

    DJANGO_ENV = 'prod'

    _config()

    env.user = 'ubuntu'
    env.hosts = ['52.14.68.5',]
    env.forward_agent = True

    CONFIG['DJANGO_ENV'] = DJANGO_ENV


def setup():
    global DJANGO_ENV
    global CONFIG

    CONFIG['USERNAME'] = env.user

    if not DJANGO_ENV:
        abort("You must specify a Django environment to set up.")

    # clone repo
    with settings(warn_only=True):
        run("mkdir -p %(DJANGO_ENV)s" % CONFIG)
    with cd('%(DJANGO_ENV)s' % CONFIG):
        run('git clone %(REMOTE_SOURCE_REPO)s' % CONFIG)

    # create server directory
    sudo("mkdir -p %(SRV_DIR)s" % CONFIG)
    with settings(warn_only=True):
        sudo('mkdir -p %(SRV_DIR)s/shared/static' % CONFIG)
        sudo('mkdir -p %(SRV_DIR)s/shared/log' % CONFIG)

        # setup log
        log_file = '%(SRV_DIR)s/shared/log/prod.log' % CONFIG
        sudo('touch ' + log_file)
        sudo('chmod 664 ' + log_file)

    # set server directory ownership
    sudo("chown -R %(USERNAME)s:www-data %(SRV_DIR)s" % CONFIG)

    # create virtualenv
    run ('virtualenv --no-site-packages %(SRV_DIR)s/virtualenv' % CONFIG)


def deploy():
    global DJANGO_ENV
    global CONFIG

    if not DJANGO_ENV:
        abort("You must specify a Django environment to set up.")

    # tests must pass to continue
    local('./manage.py test')

    now = datetime.now()
    CONFIG['current_date'] = "%d-%02d-%02d-%02d-%02d-%02d" % (
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second
    )

    # pull git repo on server
    run('cd %(SRV_SOURCE_REPO)s; git pull' % CONFIG)

    # use git archive to copy files from repo to dated release dir
    run('''cd %(SRV_SOURCE_REPO)s;
           git checkout-index --prefix=%(SRV_DIR)s/releases/%(current_date)s/%(REPO_NAME)s/ -a'''
         % CONFIG)

    # install virtualenv dependencies
    run('''source %(SRV_DIR)s/virtualenv/bin/activate;
           pip install -r %(SRV_DIR)s/releases/%(current_date)s/%(REPO_NAME)s/requirements.txt'''
         % CONFIG)

    # remove old symlink
    with settings(warn_only=True):
        run('rm %(SRV_DIR)s/current' % CONFIG)

    # symlink current to dated release
    run('ln -s %(SRV_DIR)s/releases/%(current_date)s %(SRV_DIR)s/current' % CONFIG)

    # copy apache config file
    run('sudo cp %(SRV_SOURCE_REPO)s/%(HTTP_CONF_FILE)s %(APACHE_CONF_DIR)s/sites-available/%(DJANGO_ENV)s.%(REPO_NAME)s.conf.%(current_date)s'
         % CONFIG)

    # remove old config symlink
    with settings(warn_only=True):
        run('sudo rm %(APACHE_CONF_DIR)s/sites-enabled/%(DJANGO_ENV)s.%(REPO_NAME)s.conf' % CONFIG)

    # symlink current to dated config
    run('sudo ln -s %(APACHE_CONF_DIR)s/sites-available/%(DJANGO_ENV)s.%(REPO_NAME)s.conf.%(current_date)s %(APACHE_CONF_DIR)s/sites-enabled/%(DJANGO_ENV)s.%(REPO_NAME)s.conf'
         % CONFIG)

    # reload Apache
    run('sudo service apache2 reload')

    # collect static files
    manage('collectstatic  --clear --noinput')

    # update database if necessary
    manage('migrate')


def manage(command):
    CONFIG['COMMAND'] = command
    with cd('%(SRV_DIR)s/current/%(REPO_NAME)s' % CONFIG):
        run('source %(SRV_DIR)s/virtualenv/bin/activate && ./manage.py %(COMMAND)s --settings=publicmeetings.settings.%(DJANGO_ENV)s'
             % CONFIG)


def test():
    global DJANGO_ENV

    if not DJANGO_ENV:
        abort("You must specify a Django environment to test.")

    # check hostname
    run("hostname")

    # run whoami as user
    run("whoami")

    # run whoami as root
    run("sudo whoami")
