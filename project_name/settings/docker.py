# Python imports
import os

# fetch the production settings
from .production import *


# make Django work correctly behind the nginx proxy
# nginx **must** set the appropriate header!
ALLOWED_HOSTS = os.environ.get('DPS_DJANGO_ALLOWED_HOSTS', '{{ project_name }}').split()
USE_X_FORWARDED_HOST = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'dps_docker_default': {
            'format': '%(asctime)-19s %(levelname)-8s [%(process)d] [%(name)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'docker_stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'dps_docker_default',
            'level': 'DEBUG',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        # all Django logs should end up here...
        'django': {
            # Django's 'mail_admins' handler is removed!
            'handlers': ['docker_stdout'],
            'level': os.environ.get('DPS_DJANGO_LOGGING_LEVEL', 'INFO').upper(),
            # Whatever got catched here will not propagate to the root logger
            'propagate': False,
        },
    },
    # the 'root' logger is just redefined to make it compatible with Docker
    'root': {
        'handlers': ['docker_stdout'],
        'level': os.environ.get('DPS_DJANGO_LOGGING_LEVEL', 'INFO').upper(),
    },
}
