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
    documentation on STATIC_ROOT <https://docs.djangoproject.com/en/1.11/ref/settings/#static-root>`_
    and `this howto on static files <https://docs.djangoproject.com/en/1.11/howto/static-files/>`_.

``MEDIA_ROOT``
    The directory for user-uploaded files. It will be set to
    ``[project_root]/run/media``. Please refer to the `official settings
    documentation on MEDIA_ROOT <https://docs.djangoproject.com/en/1.11/ref/settings/#media-root>`_.

``STATICFILES_DIRS``
    Django will look in these locations for additional static
    assets to collect. Our settings module adds ``[project_root]/static`` to
    the list. See the `official settings documentation on STATICFILES_DIRS
    <https://docs.djangoproject.com/en/1.11/ref/settings/#staticfiles-dirs>`_
    for more details.

``PROJECT_TEMPLATES``
    Django will look in these locations for additional
    templates. Our settings module adds ``[project_root]/templates``.

    This setting was changed to reflect the changes in Django 1.8: Django
    features the possibility to use multiple different template engines. This
    is controlled with the TEMPLATES directive and represents the old
    TEMPLATE_DIRS directive. See the
    `official settings documentation on TEMPLATE_DIRS
    <https://docs.djangoproject.com/en/1.11/ref/settings/#template-dirs>`_
    for more details.

Application Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

``DEFAULT_APPS``
    These are the default apps of ``django-admin startproject``. Please note
    that this is no official setting. Django operates with ``INSTALLED_APPS``,
    which will be set in *dev.py*.

``MIDDLEWARE``
    *(new in 1.2; Django 1.10)*
    These are the default middleware classes, directly taken from the default
    settings created by ``django-admin startproject``. See the
    `official settings documentation on MIDDLEWARE_CLASSES 
    <https://docs.djangoproject.com/en/1.11/ref/settings/#middleware>`_
    for more details. (Please note: This was used to be called
    *MIDDLEWARE_CLASSES*)

``TEMPLATES``
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
    <https://docs.djangoproject.com/en/1.11/ref/settings/#admins>`_.

``MANAGERS``
    You will have to fill this setting yourself, please refer to `official
    settings documentation on MANAGERS
    <https://docs.djangoproject.com/en/1.11/ref/settings/#managers>`_.

Django Running Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``WSGI_APPLICATION``
    This setting determines the path to the WSGI-application. We'll use the
    default one, so this setting is set to ``[project_name].wsgi.application``.

``ROOT_URLCONF``
    Determines the root URLconf. Set to ``[project_name].urls``. See `official
    settings documentation on ROOT_URLCONF
    <https://docs.djangoproject.com/en/1.11/ref/settings/#root-urlconf>`_.

``SITE_ID``
    *(removed in 1.2)*
    A unique ID of the site. See `official settings documentation on SITE_ID
    <https://docs.djangoproject.com/en/1.11/ref/settings/#site-id>`_.

``STATIC_URL``
    Determines, under which URL static files are served. You will want to
    adjust this in a production scenario. Our default value is ``/static/``.
    See `official settings documentation on STATIC_URL
    <https://docs.djangoproject.com/en/1.11/ref/settings/#static-url>`_.

``MEDIA_URL``
    Determines, under which URL media files are served. You will want to
    adjust this in a production scenario. Our default value is ``/media/``.
    See `official settings documentation on MEDIA_URL
    <https://docs.djangoproject.com/en/1.11/ref/settings/#media-url>`_.

Debug Configuration
^^^^^^^^^^^^^^^^^^^

``DEBUG``
    Activates debugging. In this file, this is set to ``False``, because these
    are our common settings, which are shared between all configurations. We
    just want debugging while we are developing, so debugging will be activated
    in *dev.py*. See `official settings documentation on DEBUG
    <https://docs.djangoproject.com/en/1.11/ref/settings/#debug>`_ for additional
    information.

Internationalization
^^^^^^^^^^^^^^^^^^^^

``LANGUAGE_CODE``
    *(removed in 1.3)*

``TIME_ZONE``
    *(removed in 1.3)*

``USE_I18N``
    *(modified in 1.2:* ``False`` *)*
    The setting is activated in ``i18n.py``.

``USE_L10N``
    *(removed in 1.3)*

``USE_TZ``
    *(removed in 1.3)*


development.py
--------------

*(modified in 1.2: renamed* ``dev.py`` *to* ``development.py`` *)*
This file contains development settings. Plase note, that ``manage.py`` will
now automatically use this setting-file as its default, while ``wsgi.py``
still refers to ``production.py``.

Debug Configuration
^^^^^^^^^^^^^^^^^^^

``DEBUG``
    We are developing, so activate debugging.

``ALLOWED_HOSTS``
    *(new in 1.2)*
    Allow all hostnames to be used to access the server/project. See `official
    settings documentation on ALLOWED_HOSTS
    <https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts>`_.

``LOGIN_URL``
    *(new in 1.3)*
    The URL of Django's built-in login view. See `official
    settings documentation on LOGIN_URL
    <https://docs.djangoproject.com/en/1.11/ref/settings/#login-url>`_.

``LOGIN_REDIRECT_URL``
    *(new in 1.3)*
    Django will redirect the user to this URL after login, if no specific URL is given.
    See `official settings documentation on LOGIN_REDIRECT_URL
    <https://docs.djangoproject.com/en/1.11/ref/settings/#login-redirect-url>`_.

``LOGOUT_REDIRECT_URL``
    *(new in 1.3)*
    Django will redirect the user to this URL after logout, if no specific URL is given.
    See `official settings documentation on LOGIN_REDIRECT_URL
    <https://docs.djangoproject.com/en/1.11/ref/settings/#login-redirect-url>`_.

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


i18n.py
-------

*(created in 1.3)*
This file contains all settings, that affect internationalisation (i18n). These
settings were taken from other parts of the configuration (see ``common.py``).
The ``LocaleMiddleware`` will automatically be inserted into the ``MIDDLEWARE``
list.

The i18n-settings are not included by default. They have to be imported in 
``development.py`` or ``production.py``.

``LANGUAGE_CODE``
    This is the default language of your project. Django will fall back to this
    language, if the localization-middleware can't determine the user's
    preferred language. See `official settings documentation on
    LANGUAGE_CODE <https://docs.djangoproject.com/en/1.11/ref/settings/#language-code>`_.

``TIME_ZONE``
    Sets the time zone of this project. See `official settings documentation
    on TIME_ZONE
    <https://docs.djangoproject.com/en/1.11/ref/settings/#time-zone>`_.

``USE_I18N``
    Activates Django's translation system. See `official settings documentation
    on USE_I18N
    <https://docs.djangoproject.com/en/1.11/ref/settings/#use-i18n>`_.

``USE_L10N``
    Activates Django's localization engine. See `official settings documentation
    on USE_L10N
    <https://docs.djangoproject.com/en/1.11/ref/settings/#use-l10n>`_.

``USE_TZ``
    Make datetimes timezone aware. See `official settings documentation on
    USE_TZ
    <https://docs.djangoproject.com/en/1.11/ref/settings/#use-tz>`_.

``LANGUAGES``
    A list of supported languages. Django will only provide translation for
    these. See `official settings documentation on
    LANGUAGES
    <https://docs.djangoproject.com/en/1.11/ref/settings/#languages>`_.

``LOCALE_PATHS``
    A list of file system locations, to look for translations. See `official
    settings documentation on LOCALE_PATHS
    <https://docs.djangoproject.com/en/1.11/ref/settings/#locale-paths>`_.
    Please note: Django's ``LocaleMiddleware`` will automatically look for 
    translation files in each apps ``locale`` directory, so they don't need
    to be added here.


production.py
-------------

*(modified in 1.2)*
This file should contain production settings. Currently, it just reverts some
development specific configuration values, ``DEBUG`` and ``ALLOWED_HOSTS``.
Please note, that the behaviour of ``manage.py`` changed: It now uses the 
settings in ``development.py`` automatically, while ``[project_root]/wsgi.py``
refers to the settings in ``production.py``.


djangodefault.py
----------------

*(removed in 1.2)*
This are the saved settings from ``django-admin startproject``. We just keep
them for completeness, these settings are not actually used.
