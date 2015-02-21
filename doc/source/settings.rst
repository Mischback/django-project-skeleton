.. _label-project-settings:

Settings
========


common.py
---------

Path Configuration
^^^^^^^^^^^^^^^^^^

``DJANGO_ROOT``
    Absolute path of the projects Django directory

``PROJECT_ROOT``
    Absolute path of the project directory

``SITE_NAME``
    The name of our project

``STATIC_ROOT``
    The directory to collect static files into. It will be set to
    ``[project_root]/run/static``. Please refer to the `official settings
    documentation on STATIC_ROOT <https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-STATIC_ROOT>`_
    and `this howto on static files <https://docs.djangoproject.com/en/1.7/howto/static-files/>`_.

``MEDIA_ROOT``
    The directory for user-uploaded files. It will be set to
    ``[project_root]/run/media``. Please refer to the `official settings
    documentation on MEDIA_ROOT <https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-MEDIA_ROOT>`_.

``STATICFILES_DIRS``
    Django will look in these locations for additional static
    assets to collect. Our settings module adds ``[project_root]/static`` to
    the list. See the `official settings documentation on STATICFILES_DIRS
    <https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-STATICFILES_DIRS>`_
    for more details.

``TEMPLATE_DIRS``
    Django will look in these locations for additional
    templates. Our settings module adds ``[project_root]/templates``. See the
    `official settings documentation on TEMPLATE_DIRS
    <https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-TEMPLATE_DIRS>`_
    for more details.

Application Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

``DEFAULT_APPS``
    These are the default apps of ``django-admin startproject``. Please note
    that this is no official setting. Django operates with ``INSTALLED_APPS``,
    which will be set in *dev.py*.

``MIDDLEWARE_CLASSES``
    These are the default middleware classes, directly taken from the default
    settings created by ``django-admin startproject``. See the
    `official settings documentation on MIDDLEWARE_CLASSES 
    <https://docs.djangoproject.com/en/1.7/ref/settings/#middleware-classes>`_
    for more details.

``TEMPLATE_CONTEXT_PROCESSORS``
    This setting is not included in the settings of ``django-admin startproject``
    but is added using the default values. See the `official settings
    documentation on TEMPLATE_CONTEXT_PROCESSORS 
    <https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-TEMPLATE_CONTEXT_PROCESSORS>`_
    for more details.

Security Configuration
^^^^^^^^^^^^^^^^^^^^^^

``SECRET_FILE``:

``ADMINS``:

``MANAGERS``:

Django Running Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``WSGI_APPLICATION``:

``ROOT_URLCONF``:

``SITE_ID``:

``STATIC_URL``:

``MEDIA_URL``:

Debug Configuration
^^^^^^^^^^^^^^^^^^^

``DEBUG``:

``TEMPLATE_DEBUG``:

Internationalization
^^^^^^^^^^^^^^^^^^^^

``LANGUAGE_CODE``:

``TIME_ZONE``:

``USE_I18N``:

``USE_L10N``:

``USE_TZ``:


dev.py
------

Debug Configuration
^^^^^^^^^^^^^^^^^^^

``DEBUG``:

``TEMPLATE_DEBUG``:

Database Configuration
^^^^^^^^^^^^^^^^^^^^^^

``DATABASES``:

Application Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

``INSTALLED_APPS``:


production.py
-------------


djangodefault.py
----------------
