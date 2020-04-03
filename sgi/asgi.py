"""
ASGI config for {{ project_name }} project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/asgi/

This is based on Django's default 'asgi.py', but slightly modified to be
compatible with the custom project layout provided by
'django-project-skeleton'."""

# Python imports
import os

# Django imports
from django.core.wsgi import get_asgi_application

# Provide a default settings module
# WSGI is used to deploy the project, so the default value are the production
# settings. This may be overwritten in actual deployment setups.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

# actually expose an application
application = get_asgi_application()
