# public meetings Django app


## Setup

### MySQL
1.  [Download](http://dev.mysql.com/downloads/mysql/) and install
2. `export PATH=/usr/local/mysql/bin:$PATH`

#### [Reset root password](http://dev.mysql.com/doc/refman/5.7/en/resetting-permissions.html)
1. `mysql -u root -p` and enter temporary password
2. `ALTER USER 'root'@'localhost' IDENTIFIED BY '<password>';`

### Python package management
1. `sudo easy_install pip`
2. `sudo pip install virtualenv virtualenvwrapper`

 - for OS X 10.11 El Capitan & MacOS 01.12 Sierra, append `--ignore-installed six` to the above

4. [Update shell startup file for virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#shell-startup-file)

### Make virtual environment
* `mkvirtualenv publicmeetings`

### Django project
1. `git clone git@github.com:publicmeetings/app-django.git`
2. `pip install -r requirements.txt`
3. `mysql -u root -p < etc/mysql/dev.sql`
4. `./manage.py migrate`
5. `./manage.py createsuperuser --username=<your_username>`
6. `./manage.py runserver`

Next time, run `workon publicmeetings` to load the virtual environment.


## Test

`./manage.py test`
