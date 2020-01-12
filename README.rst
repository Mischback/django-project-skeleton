django-project-skeleton
=======================

**django-project-skeleton** is my skeleton for Django projects. It provides a
directory structure for Django projects during development and deployment.


Meta
----

Author:
    Mischback

Contributors:
    `agirardeaudale <https://github.com/agirardeuadale>`_,
    `jmrbcu <https://github.com/jmrbcu>`_

Status:
    maintained, in development

Version:
    1.4

Django Version:
    3.0, 2.2, 2.1, 2.0, 1.11


Usage
-----

To use this repository just use the ``template`` option of `django-admin
<https://docs.djangoproject.com/en/2.2/ref/django-admin/#startproject>`_::

    $ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/master.zip [projectname]

If you wish to automagically fill the ``apache2_vhost.sample`` the command is::

    $ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/master.zip --name apache2_vhost.sample [projectname]


Documentation
-------------

You can see the documentation over at **Read the Docs**: `django-project-skeleton
<http://django-project-skeleton.readthedocs.org/en/stable/>`_
