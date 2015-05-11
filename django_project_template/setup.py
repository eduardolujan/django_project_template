#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django_project_template',
    version='1.0',
    description="",
    author="Lincoln Loop",
    author_email='info@lincolnloop.com',
    url='',
    packages=find_packages(),
    package_data={'django_project_template': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
