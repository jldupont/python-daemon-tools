#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__fileid__  = "$Id$"
__email     = "python (at) jldupont.com"

import sys
import textwrap
from setuptools import setup, find_packages

# CUSTOMIZE HERE
#  Should be available through the Eclipse project
import python_daemon_tools as main_module

short_description, long_description = ( 
    textwrap.dedent(d).strip()
    for d in main_module.__doc__.split('\n\n', 1) )


__classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: Public Domain',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    ]

__dependencies = ['python_daemon']

setup(
    name = "python_daemon_tools",
    description      = short_description,
    author_email     = __email,
    author           = __author__,
    url              = main_module.__doc_url,
    long_description = long_description,
    version          = main_module.__version__,
    package_data     = {'':['*.*']},
    packages         = find_packages(),
    classifiers      = __classifiers,
    install_requires = __dependencies,
    tests_require    = ['MiniMock >=1.0',],
    test_suite       = ['tests.suite'],
    zip_safe         = True,
)

