.. django-project-skeleton documentation master file, created by
   sphinx-quickstart on Sat Feb 21 16:55:55 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

django-project-skeleton
=======================

**django-project-skeleton** is my skeleton for Django projects. It provides a
directory structure for Django projects during development and deployment. This
structure is based on research and own experience of developing Django apps.

**Please note:** This is *my* skeleton and is developed to fit my very own
needs for new Django projects. Please feel free to modify it to your own
requirements but be aware that no changes will be made, that **I** do not
consider usefull.

**Additional note:** As of this writing, Django 1.8 is used. So I can only
guarantee that this is working with this version.

Notable Features
----------------

* prepared directory structure
* modular settings with sane default values
* prepared sample configuration for *Apache2*-deployment with *mod_wsgi*
* including ``.gitignore``-files to help getting started with *Git*

Contents
--------

.. toctree::
    :maxdepth: 2

    quickstart
    structure
    settings
    apache2_vhost
    versions
