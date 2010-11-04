#!/usr/bin/env python
from setuptools import setup, find_packages

__author__ = 'Brian Lamar'

setup(	
	name = 'mywsgi',
	version = '0.1',
	author = __author__,
	packages = find_packages(),
	install_requires = ['gevent', 'python-daemonhelper'],
	entry_points = '''
	[console_scripts]
	mywsgi = mywsgi.daemon:main
	'''
)

