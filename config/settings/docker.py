# Python imports
import os

# fetch the production settings
from .production import *


# Make Django work correctly behind the Nginx proxy
# Nginx **must** set the appropriate header!
# In the current setup, Nginx sets the "Host" header to the "server_name".
ALLOWED_HOSTS = os.environ.get('DPS_SERVER_NAME', 'localhost').split()
#USE_X_FORWARDED_HOST = True

# Logging is set up in Gunicorn's configuration
LOGGING_CONFIG=None
