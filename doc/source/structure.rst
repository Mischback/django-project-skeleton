.. _label-project-structure:

Project Structure
=================

The *normal* Django workflow, as it is described `in the official Django
tutorial  <https://docs.djangoproject.com/en/1.11/intro/tutorial01/#creating-a-project>`_
starts a project with the command::

    $ django-admin startproject [projectname]

Your project will look like this::

    
    [projectname]/
    ├── [projectname]/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py

However, the ``startproject``-command takes an optional argument ``template``
which can be used to specify a project template to be used for project
creation (see `Django documentation
<https://docs.djangoproject.com/en/1.11/ref/django-admin/#startproject`_).

The ``template``-argument works with paths on your local machine, but also
supports URLs. So you can easily fetch this skeleton from **GitHub** using this
command::

    $ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/development.zip [projectname]

Your project will look like this::

    [projectname]/                  <- project root
    ├── [projectname]/              <- Django root
    │   ├── __init__.py
    │   ├── settings/
    │   │   ├── common.py
    │   │   ├── development.py
    │   │   ├── i18n.py
    │   │   ├── __init__.py
    │   │   └── production.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── apps/
    │   └── __init__.py
    ├── configs/
    │   ├── apache2_vhost.sample
    │   └── README
    ├── doc/
    │   ├── Makefile
    │   └── source/
    │       └── *snap*
    ├── manage.py
    ├── README.rst
    ├── run/
    │   ├── media/
    │   │   └── README
    │   ├── README
    │   └── static/
    │       └── README
    ├── static/
    │   └── README
    └── templates/
        ├── base.html
        ├── core
        │   └── login.html
        └── README


Django Root
-----------

::

    [projectname]/                  <- project root
    ├── [projectname]/              <- Django root
    │   ├── __init__.py
    │   ├── settings/
    │   │   ├── common.py
    │   │   ├── development.py
    │   │   ├── i18n.py
    │   │   ├── __init__.py
    │   │   └── production.py
    │   ├── urls.py
    │   └── wsgi.py
    └── *snap*

The Django root directory will be named according to the project name you
specified in ``django-admin startproject [projectname]``. This directory is the
project's connection with Django.

``[projectname]/settings/``
    Instead of a plain *settings*-file, the configuration is split into several
    files in this Python module. For an in-depth documentation of these
    settings see :ref:`label-project-settings`.

``[projectname]/urls.py``
    The root URL configuration of the project. The only configured set of urls
    is the admin-application. For background information see `The Django Book
    Chapter 3 <http://www.djangobook.com/en/2.0/chapter03.html>`_ and `The
    Django Book Chapter 8 <http://www.djangobook.com/en/2.0/chapter08.html>`_.

``[projectname]/wsgi.py``
    Deploying Django makes use of WSGI, the Pythonic way of deploying web
    applications. See the `official settings documentation on WSGI
    <https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/>`_ for more
    details. The default WSGI-application is modified to use our
    ``settings``-module.


apps/
-----

::

    [projectname]/                  <- project root
    ├── *snap*
    ├── apps/
    │   └── __init__.py
    └── *snap*

This directory is used for custom applications. You can safely remove this
directory, if you do not plan to develop custom applications. Most of a
Django project's apps will be installed into the Python path and not be kept
in your project root.


configs/
--------

This directory contains configuration files for deployment. Now only a
configuration file for deployment with **Apache2** and **mod_wsgi** is
provided.

::

    [projectname]/                  <- project root
    ├── *snap*
    ├── configs/
    │   ├── apache2_vhost.sample
    │   └── README
    └── *snap*

**Please note:** It is strongly advised to keep your actual server
configuration private. Therefore a ``.gitignore``-file is provided, which will
only include files ending with the suffix ``.sample`` into *Git*.

For a brief overview of the ``configs/apach2_vhost.sample`` refer to
:ref:`label-apache2-vhost`.


doc/
----

::

    [projectname]/                  <- project root
    ├── *snap*
    ├── doc/
    │   ├── Makefile
    │   └── source/
    │       └── *snap*
    └── *snap*

This directory contains the source files for this documentation.

You can safely remove this directory, if you just want to use the skeleton for
your own project.


run/
----

::

    [projectname]/                  <- project root
    ├── *snap*
    ├── run/
    │   ├── media/
    │   │   └── README
    │   ├── README
    │   └── static/
    │       └── README
    └── *snap*

This directory contains necessary files for running Django. All these files
may contain sensible or useless information, so you will not want to keep this
files in version control. A ``.gitignore``-file is prepared.

This directory will contain the SQLite database file (if you keep the provided
``dev``-settings) and the *SECRET_KEY* of Django. For a detailled explanation
see :ref:`label-project-settings`.

``run/media/``
    Django uses a special folder to store user-provided files (uploads). In the
    settings-module of this skeleton this directory is set as ``MEDIA_ROOT``.

``run/static/``
    Similar to media files, all static assets (i.e. stylesheets, javascript
    files, images) are served from a special directory.


static/ and templates/
----------------------

::

    [projectname]/                  <- project root
    ├── *snap*
    ├── static/
    │   └── README
    └── templates/
        ├── base.html
        ├── core
        │   └── login.html
        └── README

These directories are used for project wide files, meaning project wide static
assets and templates.

``static/``
    This directory is used to provide our project wide static assets. Please
    refer to `the Django documentation
    <https://docs.djangoproject.com/en/1.11/howto/static-files/#configuring-static-files>`_
    for more details. :ref:`label-project-settings` documents the
    ``STATICFILES_DIRS``-setting.

``templates/``
    This directory is used to provide our project wide templates.
    :ref:`label-project-settings` documents the ``TEMPLATE_DIRS``-setting.
    Please note, that there are two basic templates are already included. These
    are used to enable a very basic login functionality for the project.
