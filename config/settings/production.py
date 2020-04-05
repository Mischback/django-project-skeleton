# Python imports
import os

# fetch the common settings
from .common import *


# ##### APPLICATION CONFIGURATION #########################

# You will have to determine, which hostnames should be served by Django
# Determines, which hostnames should be served by Django.
# DPS_DJANGO_ALLOWED_HOSTS may contain a list of (acceptable) hostnames, while
# DPS_SERVER_NAME may only contain one hostname, as this value also determines
# the actual hostname, that is used by Nginx.
#
# If neither DPS_DJANGO_ALLOWED_HOSTS nor DPS_SERVER_NAME are provided, this
# will be an empty list and thus, no host will be served, rendering Django
# effectively useless.
ALLOWED_HOSTS = list(
    set(
        os.environ.get('DPS_DJANGO_ALLOWED_HOSTS', '').split() +
        os.environ.get('DPS_SERVER_NAME', '').split()
    )
)

INSTALLED_APPS = DEFAULT_APPS

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Don't let Django configure logging in a production environment.
# Most probably, configuring logging should be done by WSGI Server, i.e.
# Gunicorn or uWSGI.
# For Docker-based deployments, logging is configured in 'gunicorn_conf.py'.
#
# Without setting LOGGING_CONFIG to 'None', Django will setup Python's logging
# module, as described https://docs.djangoproject.com/en/3.0/topics/logging/#default-logging-configuration
LOGGING_CONFIG=None

# ##### SECURITY CONFIGURATION ############################

# TODO: Make sure, that sensitive information uses https
# TODO: Evaluate the following settings, before uncommenting them
# redirects all requests to https
# SECURE_SSL_REDIRECT = True
# session cookies will only be set, if https is used
# SESSION_COOKIE_SECURE = True
# how long is a session cookie valid?
# SESSION_COOKIE_AGE = 1209600

# validates passwords (very low security, but hey...)
# AUTH_PASSWORD_VALIDATORS = [
#    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
#    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
#    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
#    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
# ]

# the email address, these error notifications to admins come from
# SERVER_EMAIL = 'root@localhost'

# how many days a password reset should work. I'd say even one day is too long
# PASSWORD_RESET_TIMEOUT_DAYS = 1
