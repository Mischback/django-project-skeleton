# Python imports
import logging
import os
import sys

logger = logging.getLogger(__name__)


# ##### PATH CONFIGURATION ################################

# fetch Django's project directory
DJANGO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# fetch the project_root
PROJECT_ROOT = os.path.dirname(DJANGO_ROOT)

# the name of the whole site
SITE_NAME = os.path.basename(DJANGO_ROOT)

# collect static files here
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'run', 'static')

# collect media files here
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'run', 'media')

# look for static assets here
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

# look for templates here
# This is an internal setting, used in the TEMPLATES directive
PROJECT_TEMPLATES = [
    os.path.join(PROJECT_ROOT, 'templates'),
]

# add apps/ to the Python path
sys.path.append(os.path.normpath(os.path.join(PROJECT_ROOT, 'apps')))


# ##### APPLICATION CONFIGURATION #########################

# these are the apps
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# template stuff
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

# the default WSGI application
WSGI_APPLICATION = os.environ.get(
    'DPS_DJANGO_WSGI_APP',
    '{}.wsgi.application'.format(SITE_NAME)
)

# the root URL configuration
ROOT_URLCONF = '{}.urls'.format(SITE_NAME)

# the URL for static files
STATIC_URL = os.environ.get('DPS_DJANGO_STATIC_URL', '/static/')

# the URL for media files
MEDIA_URL = os.environ.get('DPS_DJANGO_MEDIA_URL', '/media/')

# adjust the minimal login
LOGIN_URL = 'core_login'
LOGIN_REDIRECT_URL = os.environ.get('DPS_DJANGO_LOGIN_REDIRECT_URL', '/')
LOGOUT_REDIRECT_URL = os.environ.get('DPS_DJANGO_LOGOUT_REDIRECT_URL', 'core_login')

# Internationalization
USE_I18N = False

# uncomment the following line to include i18n
# from .i18n import *


# ##### SECURITY CONFIGURATION ############################

# We store the secret key here
# The required SECRET_KEY is fetched at the end of this file
SECRET_FILE = os.path.normpath(os.path.join(PROJECT_ROOT, 'run', 'SECRET.key'))

# these persons receive error notification
ADMINS = (
    ('your name', 'your_name@example.com'),
)
MANAGERS = ADMINS


# ##### DEBUG CONFIGURATION ###############################
DEBUG = False


logger.debug('Trying to fetch SECRET_KEY from the environment...')
SECRET_KEY = os.environ.get('DPS_DJANGO_SECRET_KEY')
if SECRET_KEY is None:
    logger.debug('Could not find key in the environment!')

    logger.debug('Trying to read SECRET_KEY from SECRET_FILE...')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
        logger.info('Read SECRET_KEY from SECRET_FILE.')
    except IOError:
        logger.debug('Could not open SECRET_FILE ({})!'.format(SECRET_FILE))

        try:
            from django.utils.crypto import get_random_string
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
            SECRET_KEY = get_random_string(50, chars)
            with open(SECRET_FILE, 'w') as f:
                f.write(SECRET_KEY)

            logger.info('Generated a new SECRET_KEY and stored it in SECRET_FILE ({})!'.format(SECRET_FILE))
        except IOError:
            logger.exception('Could not open SECRET_FILE ({}) for writing!'.format(SECRET_FILE))
            raise Exception('Could not open {} for writing!'.format(SECRET_FILE))
else:
    logger.info('Fetched SECRET_KEY from environment.')
