.. _label-project-structure:

Project Structure
=================

The *normal* Django workflow, as it is described `in the official Django
tutorial  <https://docs.djangoproject.com/en/1.7/intro/tutorial01/#creating-a-project>`_
starts a project with the command::

    $ django-admin startproject [projectname]

Your project will look like this::

    
    [projectname]
    ├── [projectname]
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

    [projectname]
    ├── [projectname]
    │   ├── __init__.py
    │   ├── settings
    │   │   ├── common.py
    │   │   ├── dev.py
    │   │   ├── djangodefault.py
    │   │   ├── __init__.py
    │   │   └── production.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── configs
    │   ├── apache2_vhost.sample
    │   └── README
    ├── doc
    │   ├── Makefile
    │   └── source
    │       └── *snap*
    ├── manage.py
    ├── README.rst
    ├── run
    │   ├── media
    │   │   └── README
    │   ├── README
    │   └── static
    │       └── README
    ├── static
    │   └── README
    └── templates
        └── README

foobar
