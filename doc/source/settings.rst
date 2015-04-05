.. _label-project-settings:

Settings
========


common.py
---------

This file contains settings which are shared between development- and
production-settings. The provide sane defaults for developing and a solid base
for production settings.

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
    documentation on STATIC_ROOT <https://docs.djangoproject.com/en/1.8/ref/settings/#static-root>`_
    and `this howto on static files <https://docs.djangoproject.com/en/1.8/howto/static-files/>`_.

``MEDIA_ROOT``
    The directory for user-uploaded files. It will be set to
    ``[project_root]/run/media``. Please refer to the `official settings
    documentation on MEDIA_ROOT <https://docs.djangoproject.com/en/1.8/ref/settings/#media-root>`_.

``STATICFILES_DIRS``
    Django will look in these locations for additional static
    assets to collect. Our settings module adds ``[project_root]/static`` to
    the list. See the `official settings documentation on STATICFILES_DIRS
    <https://docs.djangoproject.com/en/1.8/ref/settings/#staticfiles-dirs>`_
    for more details.

``PROJECT_TEMPLATES``
    *(changed in 1.1)*

    Django will look in these locations for additional
    templates. Our settings module adds ``[project_root]/templates``.

    This setting was changed to reflect the changes in Django 1.8: Django
    features the possibility to use multiple different template engines. This
    is controlled with the TEMPLATES directive and represents the old
    TEMPLATE_DIRS directive. See the
    `official settings documentation on TEMPLATE_DIRS
    <https://docs.djangoproject.com/en/1.8/ref/settings/#template-dirs>`_
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
    <https://docs.djangoproject.com/en/1.8/ref/settings/#middleware-classes>`_
    for more details.

``TEMPLATES``
    *(new in 1.1; Django 1.8)*

    This setting reflects the new feature of multiple template engines, which
    was introduced in Django 1.8. The value is taken from the
    `official upgrading guide <https://docs.djangoproject.com/en/dev/ref/templates/upgrading/>`_
    and adjusted to include our project templates, defined in *PROJECT_TEMPLATES*.

Security Configuration
^^^^^^^^^^^^^^^^^^^^^^

``SECRET_FILE``
    Django uses a ``SECRET_KEY`` for security purposes. As you can clearly see,
    this is a very sensitive information. We will store this key in a file.
    This file's location is set up here. Default value is ``[project_root]/run/SECRET.key``.

``ADMINS``
    You will have to fill this setting yourself, please refer to `official
    settings documentation on ADMINS
    <https://docs.djangoproject.com/en/1.8/ref/settings/#admins>`_.

``MANAGERS``
    You will have to fill this setting yourself, please refer to `official
    settings documentation on MANAGERS
    <https://docs.djangoproject.com/en/1.8/ref/settings/#managers>`_.

Django Running Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``WSGI_APPLICATION``
    This setting determines the path to the WSGI-application. We'll use the
    default one, so this setting is set to ``[project_name].wsgi.application``.

``ROOT_URLCONF``
    Determines the root URLconf. Set to ``[project_name].urls``. See `official
    settings documentation on ROOT_URLCONF
    <https://docs.djangoproject.com/en/1.8/ref/settings/#root-urlconf>`_.

``SITE_ID``
    A unique ID of the site. See `official settings documentation on SITE_ID
    <https://docs.djangoproject.com/en/1.8/ref/settings/#site-id>`_.

``STATIC_URL``
    Determines, under which URL static files are served. You will want to
    adjust this in a production scenario. Our default value is ``/static/``.
    See `official settings documentation on STATIC_URL
    <https://docs.djangoproject.com/en/1.8/ref/settings/#static-url>`_.

``MEDIA_URL``
    Determines, under which URL media files are served. You will want to
    adjust this in a production scenario. Our default value is ``/media/``.
    See `official settings documentation on MEDIA_URL
    <https://docs.djangoproject.com/en/1.8/ref/settings/#media-url>`_.

Debug Configuration
^^^^^^^^^^^^^^^^^^^

``DEBUG``
    Activates debugging. In this file, this is set to ``False``, because these
    are our common settings, which are shared between all configurations. We
    just want debugging while we are developing, so debugging will be activated
    in *dev.py*. See `official settings documentation on DEBUG
    <https://docs.djangoproject.com/en/1.8/ref/settings/#debug>`_ for additional
    information.

Internationalization
^^^^^^^^^^^^^^^^^^^^

``LANGUAGE_CODE``
    Sets the language of this project. See `official settings documentation on
    LANGUAGE_CODE <https://docs.djangoproject.com/en/1.8/ref/settings/#language-code>`_.

``TIME_ZONE``
    Sets the time zone of this project. See `official settings documentation
    on TIME_ZONE
    <https://docs.djangoproject.com/en/1.8/ref/settings/#time-zone>`_.

``USE_I18N``
    Activates Django's translation system. See `official settings documentation
    on USE_I18N
    <https://docs.djangoproject.com/en/1.8/ref/settings/#use-i18n>`_.

``USE_L10N``
    Activates Django's localization engine. See `official settings documentation
    on USE_L10N
    <https://docs.djangoproject.com/en/1.8/ref/settings/#use-l10n>`_.

``USE_TZ``
    Make datetimes timezone aware. See `official settings documentation on
    USE_TZ
    <https://docs.djangoproject.com/en/1.8/ref/settings/#use-tz>`_.


dev.py
------

This file contains development settings.

Debug Configuration
^^^^^^^^^^^^^^^^^^^

``DEBUG``
    We are developing, so activate debugging.

Database Configuration
^^^^^^^^^^^^^^^^^^^^^^

``DATABASES``
    I use SQLite for development. The database file will be created in 
    ``[project_root]/run/dev.sqlite3``.

Application Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

``INSTALLED_APPS``
    We have set the default apps. Now we build the (required)
    ``INSTALLED_APPS``-setting by using ``DEFAULT_APPS`` and add any app we
    need for development.


production.py
-------------

This file contains all production settings. Please note, that the current
setup leaves this empty and simply imports the dev-settings. This is done,
because we have adjusted ``manage.py`` and ``[project_root]/wsgi.py`` to use
the production settings.


djangodefault.py
----------------

This are the saved settings from ``django-admin startproject``. We just keep
them for completeness, these settings are not actually used.
