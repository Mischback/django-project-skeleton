# Python imports
import os


# bind Gunicorn to this HOST:PORT, may be a list!
# TODO: Is it really required to bind to 0.0.0.0 in Docker-based setup?
# TODO: Ensure, that :8000 ist not accessible from outside of the Docker-space
bind = '0.0.0.0:8000'
# bind = ['0.0.0.0:8000', '[::]:8000']  # provide binding for IPv4 and IPv6

# specify the number of workers
workers = os.environ.get('DPS_GUNICORN_NUM_WORKERS', 2)  # Gunicorn default: 1

# specify the class of Gunicorn's workers
# make use of threaded workers
worker_class = os.environ.get('DPS_GUNICORN_WORKER_CLASS', 'gthread')  # Gunicorn default: 'sync'

# number of threads per worker (see above)
threads = os.environ.get('DPS_GUNICORN_NUM_THREADS', 4)  # Gunicorn default: 1

# limit the lifespan of a worker by the number of handled requests
# this might prevent memory leaks
max_requests = 500  # Gunicorn default: 0 (unlimited)
max_requests_jitter = 25  # Gunicorn default: 0 (new in Gunicorn 19.2)

# number of seconds to wait for requests on a Keep-Alive connection
# this setting is **not relevant** if using the 'sync' worker-class!
keepalive = os.environ.get('DPS_GUNICORN_KEEPALIVE', 10)  # Gunicorn default: 2

# fix Gunicorn's heartbeat inside of containers
# http://docs.gunicorn.org/en/stable/faq.html#how-do-i-avoid-gunicorn-excessively-blocking-in-os-fchmod
# BLUF: have a tmpfs mount for worker_tmp_dir
# TODO: investigate the Docker image and search for a tmpfs mount (or create one!)
worker_tmp_dir = '/dev/shm'  # Gunicorn default: None

# disables the use of sendfile().
# TODO: Check this setting and research its mechanics in a setup with NGINX/Gunicorn
# sendfile = None  # Gunicorn default: None

# specify a PID file
# TODO: Check if a PID file is relevant for a Docker-based setup
# pidfile = None  # Gunicorn default: None

# Control user/group of the worker process
# TODO: Should not be necessary for a Docker-based setup, where privileges are
#   droppen in the image
# user =
# group =


### security related configuration ###
# limit_request_line = 4096  # Gunicorn default: 4096
# limit_request_fields = 100  # Gunicorn default: 100
# limit_request_field_size = 8190  # Gunicorn default: 8190

# these settings may be relevant if operating behind a proxy, that terminates HTTPS
# The DPS setup does not require this, because NGINX sets a header field that
# is evaluated by Django
# secure_scheme_headers =
# forwarded_allow_ips =


### logging related configuration ###
# Gunicorn uses Python's default logging library. Generally, the logging may be
# configured freely by passing a 'logconfig' file or 'logconfig_dict' Python
# dict.
# For this configuration, only relevant parts of the logging config are
# exposed/altered to match the Docker-based production environment.

# While running behind a reverse proxy, Gunicorn's logs will only show the
# reverse proxy's IP.
# This project's setup uses an NGINX, which sets the 'X-Forwarded-For'-header.
# See: https://stackoverflow.com/questions/25737589/gunicorn-doesnt-log-real-ip-from-nginx
access_log_format = os.environ.get(
    'DPS_GUNICORN_LOGFORMAT',
    '%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
)


logconfig_dict = {
    'version': 1,
    'disable_existing_loggers': True,
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
            #'handlers': ['docker_stdout'],
            'level': os.environ.get('DPS_DJANGO_LOGLEVEL', 'INFO').upper(),
            # Whatever got catched here will not propagate to the root logger
            #'propagate': False,
        },
        'gunicorn': {
            #'handlers': ['docker_stdout'],
            'level': os.environ.get('DPS_GUNICORN_LOGLEVEL', 'INFO').upper(),
            # Whatever got catched here will not propagate to the root logger
            #'propagate': False,
        },
        'gunicorn.access': {
            'propagate': os.environ.get('DPS_GUNICORN_SHOW_ACCESS_LOG', 'false').lower() == 'true',
        },
    },
    # the 'root' logger is just redefined to make it compatible with Docker
    'root': {
        'handlers': ['docker_stdout'],
        #'level': os.environ.get('DPS_DJANGO_LOGGING_LEVEL', 'INFO').upper(),
    },
}
