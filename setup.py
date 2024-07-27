#!/usr/bin/env python

from distutils.core import setup

setup(name='loki-python-client',
      version='1.1.0',
      description='Loki Python Client',
      author='Michael Truchard',
      author_email='mtruchard@saplingdata.com',
      url='https://github.com/sapling-data/loki-python-client',
      packages=['loki'],
      install_requires=[
        'requests'
      ]
     )