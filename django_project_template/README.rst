.. 

django_project_template
======================

Quickstart
----------

To bootstrap the project::

    virtualenv django_project_template
    source django_project_template/bin/activate
    cd path/to/django_project_template/repository
    pip install -r requirements.pip
    pip install -e .
    cp django_project_template/settings/local.py.example django_project_template/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
