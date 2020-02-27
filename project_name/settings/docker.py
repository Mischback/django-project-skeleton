# Python imports
import logging
import os

# fetch the production settings
from .production import *


class MaxLevelFilter(logging.Filter):
    """Only allow messages up to a given logging level.

    The idea is to direct any logs below a given level to stdout and above
    that level to stderr.

    This is based on
    https://stackoverflow.com/questions/1383254/logging-streamhandler-and-standard-streams
    """

    def __init__(self, max_level):
        self.max_level = getattr(logging, max_level)

    def filter(self, record):
        return record.levelno < self.max_level


# make Django work correctly behind the nginx proxy
# nginx **must** set the appropriate header!
ALLOWED_HOSTS = os.environ.get('DPS_DJANGO_ALLOWED_HOSTS', '{{ project_name }}').split()
USE_X_FORWARDED_HOST = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'max_level_filter': {
            '()': '{{ project_name }}.settings.docker.MaxLevelFilter',
            'max_level': 'WARNING',
        },
    },
    'handlers': {
        'docker_stdout': {
            'level': 'DEBUG',
            'filters': ['max_level_filter'],
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        },
        'docker_stderr': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['docker_stdout', 'docker_stderr'],
            # TODO: Make this adjustable by environment as minimal logging level
            'level': 'INFO',
        },
    },
}

logging.getLogger('django').info('Applied fixes for running Django in Docker behind nginx!')
