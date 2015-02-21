# Import some utility functions
from os.path import abspath, basename, dirname, join, normpath

# #########################################################

# ##### PATH CONFIGURATION ################################

# Fetch Django's project directory
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Fetch the project_root
PROJECT_ROOT = dirname(DJANGO_ROOT)

# The name of the whole site
SITE_NAME = basename(DJANGO_ROOT)

# Collect static files here
STATIC_ROOT = join(PROJECT_ROOT, 'run', 'static')

# Collect media files here
MEDIA_ROOT = join(PROJECT_ROOT, 'run', 'media')

# look for static assets here
STATICFILES_DIRS = [
    join(PROJECT_ROOT, 'static'),
]

# look for templates here
TEMPLATE_DIRS = [
    join(PROJECT_ROOT, 'templates'),
]


# ##### APPLICATION CONFIGURATION #########################

# This are the apps
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middlewares
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Template stuff
TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages'
]


# ##### SECURITY CONFIGURATION ############################

# We store the secret key here
# The required SECRET_KEY is fetched at the end of this file
SECRET_FILE = normpath(join(PROJECT_ROOT, 'run', 'SECRET.key'))

# These persons receive error notification
ADMINS = (
    ('your name', 'your_name@example.com'),
)
MANAGERS = ADMINS


# ##### DJANGO RUNNING CONFIGURATION ######################

# The default WSGI application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

# The root URL configuration
ROOT_URLCONF = '%s.urls' % SITE_NAME

# This site's ID
SITE_ID = 1

# The URL for static files
STATIC_URL = '/static/'

# The URL for media files
MEDIA_URL = '/media/'


# ##### DEBUG CONFIGURATION ###############################
DEBUG = False
TEMPLATE_DEBUG = DEBUG


# ##### INTERNATIONALIZATION ##############################

LANGUAGE_CODE = 'de'
TIME_ZONE = 'Europe/Berlin'

# Internationalization
USE_I18N = True

# Localisation
USE_L10N = True

# enable timezone awareness by default
USE_TZ = True


# Finally grab the SECRET KEY
try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
    try:
        from django.utils.crypto import get_random_string
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
        SECRET_KEY = get_random_string(50, chars)
        with open(SECRET_FILE, 'w') as f:
            f.write(SECRET_KEY)
    except IOError:
        raise Exception('Could not open %s for writing!' % SECRET_FILE)
