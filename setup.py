#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# Package meta-data.
NAME = 'mh-z19_exporter'
DESCRIPTION = 'Prometheus exporter for mh-z19 module'
URL = 'https://github.com/tk3fftk/mhz19-exporter'
AUTHOR = 'tk3fftk'
EMAIL = "tk3fftk@yahoo.co.jp"
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.0.1'

REQUIRED = [
    'prometheus_client',
    'mh-z19'
]

EXTRAS = {}
setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    install_requires=REQUIRED,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    keywords="exporter mh-z19",
    url=URL,
)
