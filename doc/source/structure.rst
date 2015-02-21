.. _label-project-structure:

Project Structure
=================

The *normal* Django workflow, as it is described `in the official Django
tutorial  <https://docs.djangoproject.com/en/1.7/intro/tutorial01/#creating-a-project>`_
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
<https://docs.djangoproject.com/en/1.7/ref/django-admin/#startproject-projectname-destination>`_).

The ``template``-argument works with paths on your local machine, but also
supports URLs. So you can easily fetch this skeleton from **GitHub** using this
command::

    $ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/master.zip [projectname]

Your project will look like this::

    [projectname]/                  <- project root
    ├── [projectname]/              <- Django root
    │   ├── __init__.py
    │   ├── settings/
    │   │   ├── common.py
    │   │   ├── dev.py
    │   │   ├── djangodefault.py
    │   │   ├── __init__.py
    │   │   └── production.py
    │   ├── urls.py
    │   └── wsgi.py
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
        └── README


Django Root
-----------

This directory is the project's connection with Django. It contains the
*wsgi-Application* (in ``wsgi.py``) and the *root URL configuration*
(in ``urls.py``).

Instead of a plain *settings*-file, the configuration is split into several
files in a ``settings``-module. For an in depth documentation of these settings
see :ref:`label-project-settings`.


configs/
--------

This directory contains configuration files for deployment. Now only a
configuration file for deployment with **Apache2** and **mod_wsgi** is
provided.

**Please note:** It is strongly advised to keep your actual server
configuration private. Therefore a ``.gitignore``-file is provided, which will
only include files ending with the suffix ``.sample`` into *Git*.

For a brief overview of the ``apach2_vhost.sample`` refer to
:ref:`label-apache2-vhost`.


doc/
----

This directory contains the source files for this documentation.

You can safely remove this directory, if you just want to use the skeleton for
your own project.


run/
----

This directory contains necessary files for running Django. All these files
may contain sensible or useless information, so you will not want to keep this
files in version control. A ``.gitignore``-file is prepared.

This directory will contain the SQLite database file (if you keep the provided
``dev``-settings) and the *SECRET_KEY* of Django. For a detailled explanation
see :ref:`label-project-settings`.

media/
^^^^^^

Django uses a special folder to store user-provided files (uploads). In the
settings-module of this skeleton this directory is set as ``MEDIA_ROOT``.

In a production-environment you will want to handle media files differently,
so you will not longer use this directory. Regard it as a development setting.

static/
^^^^^^^

Similar to media files, all static assets (i.e. stylesheets, javascript files,
images) are served from a special directory.

In a production-environment you will want to handle static files differently,
so you will not longer use this directory. Regard it as a development setting.


static/
-------

This directory is used to provide our project wide static assets. Please refer
to `the Django documentation
<https://docs.djangoproject.com/en/1.7/howto/static-files/#configuring-static-files>`_
for more details.


templates/
----------

This directory is used to provide our project wide templates.
