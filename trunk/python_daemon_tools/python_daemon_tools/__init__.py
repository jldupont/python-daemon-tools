r"""
python_daemon_tools: adds functionality to ``python_daemon`` package

The package python_daemon_ is very useful but lacks certain features such as:

1. The capability to ``start`` and ``stop`` a daemon
2. Assist with logging

This package adds these functionalities to ``python_daemon``.

.. _python_daemon: http://pypi.python.org/pypi/python-daemon/

"""
__author__  = "Jean-Lou Dupont"
__version__ = "0.0.1"
__doc_url   = "http://python-daemon-tools.googlecode.com/svn/trunk/python_daemon_tools/docs/html/index.html"
__fileid = "$Id$"

from runner import *