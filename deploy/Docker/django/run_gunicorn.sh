#!/bin/bash

set -euo pipefail

export DJANGO_SETTINGS_MODULE="config.settings.production"

exec gunicorn sgi.wsgi:application --config='file:/docker-bin/gunicorn_conf.py'
