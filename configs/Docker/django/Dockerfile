##############################################################################
# STAGE 01
#
# Fetching the base image and activate a virtual environment.
##############################################################################

# base this on a slim Debian image running nothing more than Python
# Why Debian and not Alpine? Personal preference of Debian-based systems.
# Additionally, Alpine is not using glibc, which might introduce problems. If
# you want your image even smaller, you may switch to an Alpine based-image.
FROM python:3.8-slim-buster as stage01_activate_venv

# create the virtual environment for our project
# TODO: the two environment variables are actually like "activating" the
# virtual environment. But they are based off a tutorial that uses
# "virtualenv" instead of "stdlib's venv". Verify, that this actually
# activates the environment.
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m venv $VIRTUAL_ENV

# update pip inside of the virtual environment
RUN pip install --upgrade pip


##############################################################################
# STAGE 02
#
# Using the requirements to build wheels for the final image.
##############################################################################
FROM stage01_activate_venv as stage02_building_wheels

# set environment variables
# TODO: Compare this to tox's settings!
# TODO: Check if these are still valid for "production"!
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements/production.txt ./requirements.txt

# build wheels from requirements
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt


##############################################################################
# STAGE 03
#
# Actually install the packages in the virtual environment.
##############################################################################
FROM stage01_activate_venv as stage03_installing_packages

# set environment variables
# TODO: Compare this to tox's settings!
# TODO: Check if these are still valid for "production"!
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

# install dependencies
COPY --from=stage02_building_wheels /wheels /wheels
RUN pip install --no-cache /wheels/* \
    && rm -rf /wheels


##############################################################################
# STAGE 04
#
# Prepare the Django environment, performing the following tasks:
#   - preparing the database by running django-admin migrate
#   - running django-admin collectstatic
##############################################################################
FROM stage03_installing_packages

# create a user to be used (meaning: we won't run with root-permissions!)
RUN useradd -u 2342 -g 65534 -s /bin/false -M pythonuser \
    && mkdir /home/pythonuser
WORKDIR /home/pythonuser
COPY . .
RUN chown -R 2342:65534 *

USER pythonuser
