.SILENT:
.PHONY: clean current default doc doc-srv help requirements requirements-force \
		serve tox \
		docker/build docker/test-build-context \
		.docker/build .docker/test-build-context

DOCKER_CMD:=docker
DOCKER_COMPOSE_CMD:=docker-compose

DPS_DOCKER_REPO:="mischback/dps"
DPS_GIT_COMMIT_BRANCH:=$(shell git rev-parse --abbrev-ref HEAD)
DPS_GIT_COMMIT_SHA1:=$(shell git rev-parse --short HEAD)

DPS_DOCKER_TAG="$(DPS_DOCKER_REPO):$(DPS_GIT_COMMIT_BRANCH)-$(DPS_GIT_COMMIT_SHA1)"


default: help
	echo ""
	echo "You need to specify a subcommand."
	exit 1


help:
	echo ""
	echo "Development utilities"
	echo "  clean        Removes all temporary files"
	echo "  current      Runs the tox-environment for the current development"
	echo "  doc          Builds the documentation using 'Sphinx'"
	echo "  doc-srv      Serves the documentation on port 8082 (and automatically builds it)"
	echo "  serve        Runs the Django development server on port 8080"
	echo "  tox          Runs complete tox test environment"
	echo ""
	echo "Docker related commands"
	echo "  Please note, that if you are not 'root', you have to do 'sudo make ...'!"
	echo ""
	echo "  docker/test-build-context"
	echo "      Builds a minimal docker container and shows the context"
	echo "      This is used to check the .dockerignore file"
	echo ""


# deletes all temporary files created by Django
clean:
	find . -iname "*.pyc" -delete
	find . -iname "__pycache__" -delete
	rm requirements/common.txt
	rm requirements/production.txt

current:
	tox -q -e util

doc:
	tox -q -e doc

doc-srv: doc
	tox -q -e doc-srv

requirements:
	tox -q -e build_requirements

requirements-force:
	touch requirements/*.in
	$(MAKE) requirements

serve:
	tox -q -e run

tox:
	tox -q

docker/build: requirements
	sudo $(MAKE) .docker/build

.docker/build:
	DPS_DOCKER_TAG=$(DPS_DOCKER_TAG) \
	$(DOCKER_COMPOSE_CMD) -f configs/Docker/docker-compose.yml build
	$(DOCKER_CMD) tag $(DPS_DOCKER_TAG) "$(DPS_DOCKER_REPO):$(DPS_GIT_COMMIT_BRANCH)-current"

docker/test-build-context:
	sudo $(MAKE) .docker/test-build-context

.docker/test-build-context:
	echo " \
		FROM busybox\n \
		COPY . /build-context\n \
		WORKDIR /build-context\n \
		CMD find ." \
	| docker build -t test-build-context -f- . \
	&& docker container run --rm test-build-context
