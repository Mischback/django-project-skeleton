.SILENT:
.PHONY: clean init tree \
		docker/test-build-context .docker/test-build-context

DOCKER_CMD:=docker

DPS_DOCKER_REPO:="mischback/dps"


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
	cp ./configs/Makefile.deployment ./Makefile

tree:
	tree -a -I ".git|.tox|doc|run" --dirsfirst

docker/test-build-context:
	sudo $(MAKE) .docker/test-build-context

.docker/test-build-context:
	echo " \
		FROM busybox\n \
		COPY . /build-context\n \
		WORKDIR /build-context\n \
		CMD find ." | \
	$(DOCKER_CMD) build -t "$(DPS_DOCKER_REPO):test-build-context" -f- . && \
	$(DOCKER_CMD) container run --rm "$(DPS_DOCKER_REPO):test-build-context"
