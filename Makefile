.SILENT:
.PHONY: clean init tree \
		docker/build docker/build-context .docker/build-context

# Docker command
DOCKER_CMD := $(shell which docker)

# Docker compose command
DOCKER_COMPOSE_CMD := $(shell which docker-compose)

# Docker related testing is performed by using tox:
#	- an environment is used to setup a testing project (docker-testing)
#	- the project is setup in the temporary directory, thus this step is
#		performed by every run
#	- the Docker build is triggered using the corresponding Makefile
#		Makefile.deployment
#	- this Makefile will automatically tag the created image
#	- to start the image, this tagging has to be reproduced here
#
# During project setup, this variable is set to the project's name.
# The described testing process will use 'dpstest' as the project's name
DPS_BUILD_NAME_PREFIX := "dpstest"
# While the image is build, the git commit's sha1 hash is used to tag the image
# Additionally, 'latest' is applied to the image aswell.
# In order to run the image, we rely on the 'latest' build.
DPS_BUILD_ID := "latest"


# deletes all temporary and unwanted files
clean:
	# clean temporary Python files
	find . -iname "*.pyc" -delete
	find . -iname "__pycache__" -delete
	# During development of django-project-skeleton, compiled requirement
	# files are needed at some points, but the (compiled) requirements should
	# not be included into version control of the skeleton.
	# However, once the repository is fetched and used as a template for
	# Django's startproject, the compiled requirements *should* be included
	# into version control, thus, they can not simply included in a .gitignore.
	rm requirements/common.txt
	rm requirements/production.txt
	rm configs/Docker/env.production

init:
	# TODO: Include some output to this function
	# create the final version of different files by removing the '.sample' suffix
	mv ./configs/apache2_vhost.sample.template ./configs/apache2_vhost.sample
	mv ./configs/Docker/django/run_gunicorn.sh.template ./configs/Docker/django/run_gunicorn.sh
	# switching the tox configuration file
	mv ./configs/tox.deployment.template ./tox.ini
	# switching the Makefile **should** be the last step
	mv ./configs/Makefile.deployment.template ./Makefile

configs/Docker/env.production:
	echo "Initializing environment file for production..."
	cp configs/Docker/env.sample configs/Docker/env.production
	sed -i "s/#DPS_DJANGO_SECRET_KEY=/DPS_DJANGO_SECRET_KEY=$(shell ./bin/generate_secret_key.sh)/" configs/Docker/env.production

docker/build: configs/Docker/env.production
	tox -q -e docker-testing

docker/build-context:
	sudo $(MAKE) .docker/build-context

docker/images:
	sudo $(MAKE) .docker/images

docker/run: docker/build
	sudo $(MAKE) .docker/run

run: docker/run

tree:
	tree -a -I ".git|.tox|doc|run" --dirsfirst -C | less -r

.docker/build-context:
	echo " \
		FROM busybox\n \
		COPY . /build-context\n \
		WORKDIR /build-context\n \
		CMD find ." | \
	$(DOCKER_CMD) build -t "$(DPS_BUILD_NAME_PREFIX)/build-context:latest" -f- . && \
	$(DOCKER_CMD) container run --rm "$(DPS_BUILD_NAME_PREFIX)/build-context:latest"

.docker/images:
	$(DOCKER_CMD) images

.docker/run:
	DPS_BUILD_NAME_PREFIX=$(DPS_BUILD_NAME_PREFIX) DPS_BUILD_ID=$(DPS_BUILD_ID) \
	$(DOCKER_COMPOSE_CMD) -f configs/Docker/docker-compose.yml up
