# fetch the production settings
from .production import *

# make Django work correctly behind the nginx proxy
# nginx **must** set the appropriate header!
ALLOWED_HOSTS = ['{{ project_name }}']
USE_X_FORWARDED_HOST = True
