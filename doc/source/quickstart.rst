Quickstart
==========

I assume you know what you are doing, so let's just do it::

    $ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/development.zip [projectname]

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

See :ref:`label-project-structure` for a detailled description of this layout.
