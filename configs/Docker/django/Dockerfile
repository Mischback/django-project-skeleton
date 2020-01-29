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


FROM base as requirements_compiler

# TODO: install the requirements for Python dependency management
# RUN pip install pip-tools

# TODO: fetch the requirements-directory
# COPY ./requirements/*.in /requirements

# TODO: actually build the requirements for production environment
# TODO: if layered/included requirements are used, the files have to be compiled
#   in the correct order.
# RUN pip-compile --generate-hashes \
#         --output-file /requirements/common.txt \
#         /requirements/common.in && \
#     pip-compile --generate-hashes \
#         --output-file /requirements/production.txt \
#         /requirements/production.in


FROM base as venv_builder

# fetch the production requirements
COPY ./requirements/production.txt ./requirements.txt
# COPY --from=requirements_compiler /requirements/production.txt ./requirements.txt

# actually install the requirements into the virtual environment
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.8-slim-buster as django_production

# create a user to be used (meaning: we won't run with root-permissions!)
RUN useradd -u 2342 -g 65534 -s /bin/false -M pythonuser && \
    mkdir /home/pythonuser
WORKDIR /home/pythonuser

# fetch the virtual environment from base
COPY --from=venv_builder --chown=2342:65534 /venv /venv

# fetch the actual project files
COPY --chown=2342:65534 . .

# drop user privileges
USER pythonuser
