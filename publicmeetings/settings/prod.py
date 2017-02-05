from .base import *

with open('/etc/django/secret_key.txt') as f:
  SECRET_KEY = f.read().strip()

SRV_SHARED_DIR = '/srv/app-django/shared/'

DEBUG = False

ALLOWED_HOSTS = ['www.publicmeetings.co']

ADMINS = [
    ('Admins', 'admins@publicmeetings.co')
]

MANAGERS = [
    ('Managers', 'managers@publicmeetings.co')
]

STATIC_ROOT = os.path.join(SRV_SHARED_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/django/my.cnf',
        },
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(SRV_SHARED_DIR, 'log/prod.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

GOOGLE_ANALYTICS_ID = ''

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = 'DENY'
