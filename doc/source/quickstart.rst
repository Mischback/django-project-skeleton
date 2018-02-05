Quickstart
==========

I assume you know what you are doing, so let's just do it::

    $ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/development.zip [projectname]

Your project will look like this::

    [projectname]/
    ├── [projectname]/
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

See :ref:`label-project-structure` for a detailled description of this layout.
