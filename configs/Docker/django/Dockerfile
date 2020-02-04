# base this on a slim Debian image running nothing more than Python
# Why Debian and not Alpine? Personal preference of Debian-based systems.
# Additionally, Alpine is not using glibc, which might introduce problems. If
# you want your image even smaller, you may switch to an Alpine based-image.

### BASE
# The purpose of this image is to prepare the virtual environment, that will
# be used to run the Django stack in the final image.
#
# This image will be discarded and is merely a build artifact, leveraging
# Docker's multistage building feature to reduce the final image size.
#
# TODO: If there are any system dependencies, including build dependencies for
#       the Python packages, they must be installed here aswell!
FROM python:3.8-slim-buster as base

# set environment variables
# TODO: Check if these are still valid for "production"!
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the virtual environment for our project
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m venv $VIRTUAL_ENV

# update pip inside of the virtual environment
RUN pip install --upgrade pip

# fetch the production requirements
# TODO: actually more than the required files will be copied. Should not be a
# problem, because this image is discarded after package installation.
COPY ./requirements/*.txt /requirements/

# actually install the requirements into the virtual environment
RUN pip install --no-cache-dir \
        -r /requirements/common.txt \
        -r /requirements/production.txt


### DJANGO_PRODUCTION
# This image starts from a default debian based Python image. The virtual
# environment for running the Django stack is copied over from BASE.
#
# TODO: If there are any system dependencies, they have to be installed
#       directly into this image.
FROM python:3.8-slim-buster as django_production

# create a user to be used (meaning: we won't run with root-permissions!)
RUN useradd -u 2342 -g 65534 -s /bin/false -M pythonuser && \
    mkdir /home/pythonuser
WORKDIR /home/pythonuser

# fetch the virtual environment from base
COPY --from=base --chown=2342:65534 /venv /venv

# fetch the actual project files
COPY --chown=2342:65534 . .

# drop user privileges
USER pythonuser
