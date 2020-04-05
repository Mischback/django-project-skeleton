#!/bin/bash

set -euo pipefail

exec gunicorn sgi.wsgi:application --config='file:/docker-bin/gunicorn_conf.py'
