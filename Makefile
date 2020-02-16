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

init:
	echo "Initialising repository..."
	cp ./configs/tox.deployment ./tox.ini
	mv ./configs/Docker/bin/django-run.deployment ./configs/Docker/bin/django-run.sh
	cp ./configs/Makefile.deployment ./Makefile

docker/build:
	tox -q -e docker-testing

docker/build-context:
	sudo $(MAKE) .docker/build-context

docker/run:
	sudo $(MAKE) .docker/run

tree:
	tree -a -I ".git|.tox|doc|run" --dirsfirst

.docker/build-context:
	echo " \
		FROM busybox\n \
		COPY . /build-context\n \
		WORKDIR /build-context\n \
		CMD find ." | \
	$(DOCKER_CMD) build -t "$(DPS_BUILD_NAME_PREFIX)/build-context:latest" -f- . && \
	$(DOCKER_CMD) container run --rm "$(DPS_BUILD_NAME_PREFIX)/build-context:latest"

.docker/run:
	DPS_BUILD_NAME_PREFIX=$(DPS_BUILD_NAME_PREFIX) DPS_BUILD_ID=$(DPS_BUILD_ID) \
	$(DOCKER_COMPOSE_CMD) -f configs/Docker/docker-compose.yml up django
