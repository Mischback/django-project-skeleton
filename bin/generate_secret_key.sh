#!/bin/sh

# This script is part of django-project-skeleton and is used to generate an
# random string to be used as SECRET_KEY for Django's configuration.
#
# Ths script is - obviously - no reimplementation of the corresponding
# function provided by Django, but should provide a value, that may be
# considered "random enough".
# The code is taken from https://gist.github.com/earthgecko/3089509 , see
# https://github.com/django/django/blob/9386586f31b8a0bccf59a1bff647cd829d4e79aa/django/core/management/utils.py#L77
# for Django's original implementation.
#
# '&' had to be removed from the available characters, because it breaks 'sed'.
#
# This script is used to generate a SECRET_KEY in the env.production file.
# That file is **NOT** under version control, for obvious reasons.

cat /dev/urandom | tr -dc 'a-zA-Z0-9!@$%^()_-' | fold -w 50 | head -n 1
