# Python imports
import os

# fetch the common settings
from .common import *

# ##### APPLICATION CONFIGURATION #########################

# allow all hosts during development
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = DEFAULT_APPS


# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'run', 'dev.sqlite3'),
    }
}


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True
