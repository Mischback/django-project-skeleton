#!/bin/bash

set -euo pipefail

# determine the scripts current working directory (CWD)
CWD="${BASH_SOURCE%/*}";
if [[ ! -d "$CWD" ]]; then CWD="$PWD"; fi

# include the script for setting the timezone
source "$CWD/set_timezone.sh"

envsubst '
    ${DPS_SERVER_NAME}
    ${DPS_STATIC_URL}
    ${DPS_UPSTREAM_KEEPALIVE_TIMEOUT}
    ${DPS_NGINX_UPSTREAM_KEEPALIVE_NUM_CONN}
    ${DPS_NGINX_UPSTREAM_KEEPALIVE_NUM_REQ}
    ${DPS_NGINX_SERVER_KEEPALIVE}
    ${DPS_NGINX_SERVER_TOKENS}
    ${DPS_NGINX_GZIP_ACTIVATION}
    ${DPS_NGINX_GZIP_COMPRESSION}
    ${DPS_NGINX_GZIP_MIN_LENGTH}
    ${DPS_NGINX_GZIP_TYPES}
    ' \
    < /docker-bin/nginx.conf.template \
    > /etc/nginx/nginx.conf

exec "$@"
