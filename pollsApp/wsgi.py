"""
WSGI config for pollsApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

import django.core.handlers.wsgi

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pollsApp.settings")

application = django.core.handlers.wsgi.WSGIHandler()

application = get_wsgi_application()
