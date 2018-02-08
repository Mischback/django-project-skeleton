LOCALPATH := ./
PYTHONPATH := $(LOCALPATH)/
PYTHON_BIN := $(VIRTUAL_ENV)/bin

DJANGO_TEST_SETTINGS_FILE := development
DJANGO_TEST_SETTINGS := {{ project_name }}.settings.$(DJANGO_TEST_SETTINGS_FILE)
DJANGO_TEST_POSTFIX := --settings=$(DJANGO_TEST_SETTINGS) --pythonpath=$(PYTHONPATH)


.PHONY: clean coverage ensure_virtual_env flake8 flake lint \
		test test/dev test/prod \
		migrate setup/dev refresh refresh/dev refresh/prod update/dev


coverage: ensure_virtual_env test
	# $(PYTHON_BIN)/coverage html
	$(PYTHON_BIN)/coverage report


clean:
	@find . -iname "*.pyc" -delete
	@find . -iname "__pycache__" -delete
	@rm -rf .coverage coverage_html


ensure_virtual_env:
	@if [ -z $$VIRTUAL_ENV ]; then \
		echo "You don't have a virtualenv enabled."; \
		echo "Please enable the virtualenv first!"; \
		exit 1; \
	fi


flake8: ensure_virtual_env
	$(PYTHON_BIN)/flake8 .

flake: flake8

lint: flake8


test: ensure_virtual_env
	@echo "Using setting file '$(DJANGO_TEST_SETTINGS_FILE)'..."
	@echo ""
	@$(PYTHON_BIN)/coverage run $(PYTHON_BIN)/django-admin.py check $(DJANGO_TEST_POSTFIX)

test/dev:
	$(MAKE) test DJANGO_TEST_SETTINGS_FILE=development

test/prod:
	$(MAKE) test DJANGO_TEST_SETTINGS_FILE=production


migrate: ensure_virtual_env
	$(PYTHON_BIN)/django-admin.py migrate $(DJANGO_TEST_POSTFIX)

setup/dev: ensure_virtual_env
	@pip install -r requirements/development.txt
	$(MAKE) migrate DJANGO_TEST_SETTINGS_FILE=development
	@echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser(username='django', email='admin@example.com', password='django')" | python manage.py shell

refresh: ensure_virtual_env
	$(MAKE) clean
	$(MAKE) migrate
	$(PYTHON_BIN)/django-admin.py collectstatic --noinput $(DJANGO_TEST_POSTFIX)

refresh/dev:
	$(MAKE) refresh DJANGO_TEST_SETTINGS_FILE=development

refresh/prod:
	$(MAKE) refresh DJANGO_TEST_SETTINGS_FILE=production

update/dev: setup/dev refresh/dev
