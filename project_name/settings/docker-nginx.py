# Python imports
import os

# fetch the production settings
from .production import *

# make Django work correctly behind the nginx proxy
# nginx **must** set the appropriate header!
ALLOWED_HOSTS = os.environ.get('DPS_DJANGO_ALLOWED_HOSTS', '{{ project_name }}').split()
USE_X_FORWARDED_HOST = True
