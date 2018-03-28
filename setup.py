#!/usr/bin/env python

import sys
try:
    from setuptools import setup,find_packages
except ImportError:
    from distutils.core import setup

import hi

setup(name='hi',
      version=hi.__version__,
      description='Fast and simple web framework for hi-nginx',
      author=hi.__author__,
      author_email=hi.__author__,
      url='https://www.hi-nginx.com/',
      py_modules=['hi'],
      packages= find_packages(),
      install_requires=['Jinja2>=2'],
      scripts=['hi.py'],
      license='GPL-v3',
      platforms='LINUX',
      )
