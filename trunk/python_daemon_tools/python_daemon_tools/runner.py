#!/usr/bin/env python
""" This module borrows heavily from ``python_daemon.runner``.

    @author: Jean-Lou Dupont
"""
__all__ = ['DaemonRunner',]

# Imports from package ``python_daemon`` available on Pypi
# --------------------------------------------------------
from python_daemon.daemon import DaemonContext
from python_daemon.pidlockfile import PIDLockFile


class DaemonRunner(object):
    """
    Controller class for a callable running in a separate background process
    
    
    """
    