#!/bin/bash

set -euo pipefail

export DJANGO_SETTINGS_MODULE="config.settings.docker"

exec gunicorn wsgi.app:application --config='file:/docker-bin/gunicorn_conf.py'
