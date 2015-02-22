.. _label-apache2-vhost:

Apache2 Virtual Host Configuration
==================================

This is an Apache2 configuration file for name based virtual hosting.

As you can see in the following listing, there are several placeholders,
that must be filled to make this work.

Usage
-----

As you may notice, there are three different types of placeholders.

``[[placeholder_name]]``
    These placeholders must be filled manually. Most noticable is line 4,
    where you **must** set the server name.

    ``ServerName    [[SERVER_NAME]]``

``${placeholder_name}``
    These placeholders are filled by Apache itsself. Only mess with them, if
    you do exactly know what you are doing.

``{{ placeholder_name }}``
    These placeholders do look familiar, don't they? These are Django
    templatetags. You may fill them manually (please refer to the provided
    resources in the comments), but you can Django let them fill them for you
    during project creation. This will render the file through Django's
    template engine and fill these placeholders::

    $ django-admin startproject --template=/path/to/template --name apache2_vhost.sample


Concept
-------

This will set up a name based virtual host that uses *mod_wsgi* to interact
with Django.

It will serve static- and media-files from the default locations set in
``settings/common.py``. This is not a production-setting, but is well suited
for development purposes.

Line 10: ``Alias /static/   {{ project_directory }}/run/static``
    Serve static files from ``STATIC_ROOT`` under ``STATIC_URL``. Note lines
    36 - 40, where the directory is made accessible for Apache.

Line 15: ``Alias /media/    {{ project_directory }}/run/media``
    Serve media files from ``MEDIA_ROOT`` under ``MEDIA_URL``. Note lines
    45 - 49, where the directory is made accessible for Apache.

The dynamic Django content is served using the *WSGI-application*. Apache2 will
use *mod_wsgi* in Daemon-mode. This is in fact the preferred way of deploying
Django with Apache2, so you will not have to mess with these settings.

Line 18: ``WSGIScriptAlias  /   {{ project_directory }}/{{ project_name }}/wsgi.py``
    This must be set to the absolute filesystem path to the *WSGI-application*.

Line 27: ``WSGIDaemonProcess ...``
    This sets the name of the daemon process. Using Django's template engine,
    this will be set to the name of your project. Please notice the
    ``python-path``-parameter. It is prepared to a virtualenv-setup, but
    frankly, it must contain the *project directory* and the path to Python's
    *site-packages*.

Line 31: ``WSGIProcessGroup ...``
    Specifies a distinct name for the daemon process's group.


Source
------

.. literalinclude:: ../../configs/apache2_vhost.sample
    :language: apache
    :linenos:

