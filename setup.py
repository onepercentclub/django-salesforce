#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# django-salesforce
#
# by Phil Christensen
# (c) 2012-2013 Freelancers Union (http://www.freelancersunion.org)
# See LICENSE.md for details
#

from distutils.core import setup
from setuptools import find_packages

import os

def get_long_description():
    path = os.path.join(os.path.dirname(__file__), 'README.rst')
    with open(path) as f:
        return f.read()

setup(
    name='django-salesforce',
    version='0.1.6.3',
    license='MIT',
    description='a Salesforce backend for Django\'s ORM',
    long_description=get_long_description(),
    url='https://github.com/freelancersunion/django-salesforce',

    author='Freelancers Union',
    author_email='devs@freelancersunion.org',
    maintainer='Phil Christensen',
    maintainer_email='phil@bubblehouse.org',

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django>=1.3,<1.4.99',
        'restkit>=4.1.2',
        'simplejson>=2.5.0',
        'oauth2>=1.5.211',
        'pytz',
    ],
)
