#!/usr/bin/env python
from setuptools import setup, find_packages

__author__ = "Brian Lamar"
__doc__ = """`mywsgi` is an attempt at a very straight-forward, no-nonsense, heavily-tested, WSGI framework for Python."""

setup(	
	name             = 'mywsgi',
	version          = '0.1',
	author           = __author__,
    description      = __doc__,
	packages         = ['mywsgi'],
	install_requires = ['gevent'],
	entry_points =   '',
)

