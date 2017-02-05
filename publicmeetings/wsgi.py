"""
WSGI config for publicmeetings project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

sys.path.insert(0, "/srv/app-django/current/app-django/")
sys.path.insert(0, "/srv/app-django/virtualenv/lib/python2.7/site-packages")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "publicmeetings.settings.prod")

application = get_wsgi_application()
