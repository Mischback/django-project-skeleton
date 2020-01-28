# base this on a slim Debian image running nothing more than Python
# Why Debian and not Alpine? Personal preference of Debian-based systems.
# Additionally, Alpine is not using glibc, which might introduce problems. If
# you want your image even smaller, you may switch to an Alpine based-image.
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
COPY ./requirements/production.txt ./requirements.txt

# actually install the requirements into the virtual environment
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.8-slim-buster

# create a user to be used (meaning: we won't run with root-permissions!)
RUN useradd -u 2342 -g 65534 -s /bin/false -M pythonuser \
    && mkdir /home/pythonuser
WORKDIR /home/pythonuser

# fetch the virtual environment from base
COPY --from=base --chown=2342:65534 /venv /venv

COPY --chown=2342:65534 . .
# RUN chown -R 2342:65534 *

USER pythonuser
