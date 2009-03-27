#!/usr/bin/env python
""" 
This module borrows heavily from python_daemon_ available at Pypi


.. _python_daemon: http://pypi.python.org/pypi/python-daemon/

@author: Jean-Lou Dupont
"""
__all__ = ['DaemonRunner',]

import errno
import signal
import os
import sys



# Imports from package ``python_daemon`` available on Pypi
# --------------------------------------------------------
try:
    from python_daemon.daemon import DaemonContext
    from python_daemon.pidlockfile import PIDLockFile
except:
    # For the Windows based development environment...
    #  This helps me with the automatic Sphinx doc generation
    computer_name = str(os.environ['computername'])
    if (computer_name != "JLDUPONT"):
        print "python_daemon_tools requires `python_daemon` package available through Pypi"
        exit(0)    


# Local imports
import python_daemon_tools.helper



class DaemonRunnerException(Exception):
    """
    DaemonRunner Exception base class
    
    Allows for easier customization of error messages.
    """
    def __init__(self, message, params=None):
        Exception.__init__(self, message)
        self.params = params


    

class DaemonRunner(object):
    """
    Controller class for a callable running in a separate background process
    
    The ``PID lock file`` is derived from ``app.name`` in the following way ::
    
        ${app.pid_directory}/${app.name}.pid
    
    and by default is located in the ``/var/run`` directory; this directory
    can be customized through the ``app.pid_directory`` attribute.
    
    The exceptions generated by this class contain `pseudo-messages` which are
    really meant as `index` to human readable messages. This way, customization
    is easier to handle.
    
    """
    def __init__(self, app, logger = None):
        """
        The parameter ``app`` must be a callable with, as minimum, the following attributes:
        
        * *name*
        * *run()* method 
        
        Optional attributes are:
        
        * *before_start()* method

        
        The parameter ``logger`` is meant to receive a compatible callable to the
        ``logging`` module. This parameter defaults to ...
        """

        
    def cmd_start(self):
        """
        Starts the daemon for ``app``
        
        The method ``app.before_start()`` is called prior to actually daemonizing;
        the method can abort the process by raising ...
        
        The method ``app.before_start()`` need not to exist (a validity check is performed).
        """
        
    def cmd_stop(self):
        """
        Stops the daemon for (the currently running) ``app`` but not before calling ``app.stop``
        """
        
    def cmd_restart(self):
        """
        Restarts the daemon for (the currently running) ``app``
        """
        self.stop()
        self.start()




