LOCALPATH := ./
PYTHONPATH := $(LOCALPATH)/
PYTHON_BIN := $(VIRTUAL_ENV)/bin

DJANGO_TEST_SETTINGS_FILE := development
DJANGO_TEST_SETTINGS := {{ project_name }}.settings.$(DJANGO_TEST_SETTINGS_FILE)
DJANGO_TEST_POSTFIX := --settings=$(DJANGO_TEST_SETTINGS) --pythonpath=$(PYTHONPATH)


.PHONY: all clean coverage ensure_virtual_env flake8 flake lint \
		test test/dev test/prod \
		migrate setup/dev refresh refresh/dev refresh/prod update/dev


all:
	@echo "Hello $(LOGNAME)! Welcome to django-project-skeleton"
	@echo ""
	@echo "  clean        Removes all temporary files"
	@echo "  coverage     Runs the tests and shows code coverage"
	@echo "  flake8       Runs flake8 to check for PEP8 compliance"
	@echo "                 = flake / lint"
	@echo "  migrate      Applies all migrations"
	@echo "  refresh      Refreshes the project by migrating the apps and"
	@echo "                 collecting static assets"
	@echo "  refresh/dev  Refreshes with development settings"
	@echo "  refresh/prod Refreshes with production settings"
	@echo "  setup/dev    Sets up a development environment by installing"
	@echo "                 necessary apps, running migrations and creating"
	@echo "                 a superuser (django::django)"
	@echo "  test         Runs the tests"
	@echo "  test/dev     Runs the tests with development settings"
	@echo "  test/prod    Runs the tests with production settings"
	@echo "  update/dev   Shortcut for setup and refresh"


# performs the tests and measures code coverage
coverage: ensure_virtual_env test
	$(PYTHON_BIN)/coverage html
	$(PYTHON_BIN)/coverage report


# deletes all temporary files created by Django
clean:
	@find . -iname "*.pyc" -delete
	@find . -iname "__pycache__" -delete
	@rm -rf .coverage coverage_html


# most of the commands can only be used inside of the virtual environment
ensure_virtual_env:
	@if [ -z $$VIRTUAL_ENV ]; then \
		echo "You don't have a virtualenv enabled."; \
		echo "Please enable the virtualenv first!"; \
		exit 1; \
	fi


# runs flake8 to check for PEP8 compliance
flake8: ensure_virtual_env
	$(PYTHON_BIN)/flake8 .

flake: flake8

lint: flake8


# runs the tests
#	While we just have a bare project layout, this is more or less a dummy.
test: ensure_virtual_env
	@echo "Using setting file '$(DJANGO_TEST_SETTINGS_FILE)'..."
	@echo ""
	@$(PYTHON_BIN)/coverage run $(PYTHON_BIN)/django-admin.py check $(DJANGO_TEST_POSTFIX)

# runs the tests with development settings
test/dev:
	$(MAKE) test DJANGO_TEST_SETTINGS_FILE=development

# runs the tests with production settings
test/prod:
	$(MAKE) test DJANGO_TEST_SETTINGS_FILE=production


# migrates the installed apps
migrate: ensure_virtual_env
	$(PYTHON_BIN)/django-admin.py migrate $(DJANGO_TEST_POSTFIX)

# sets up the development environment by installing required dependencies,
#	migrates the apps and creates a dummy user (django::django)
setup/dev: ensure_virtual_env
	@pip install -r requirements/development.txt
	$(MAKE) migrate DJANGO_TEST_SETTINGS_FILE=development
	@echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser(username='django', email='admin@example.com', password='django')" | python manage.py shell

# refreshes the project by migrating and collecting static assets
refresh: ensure_virtual_env
	$(MAKE) clean
	$(MAKE) migrate
	$(PYTHON_BIN)/django-admin.py collectstatic --noinput $(DJANGO_TEST_POSTFIX)

# refreshes with development settings
refresh/dev:
	$(MAKE) refresh DJANGO_TEST_SETTINGS_FILE=development

# refreshes with production settings
refresh/prod:
	$(MAKE) refresh DJANGO_TEST_SETTINGS_FILE=production

update/dev: setup/dev refresh/dev
