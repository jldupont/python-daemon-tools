#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid__  = "$Id$"

__all__ = ['getDefault', 'xcLogger']


import sys
import logging
import logging.handlers

def getDefault( name, include_console = False, include_syslog = False ):
    """ 
    Returns a simple cross-platform logger

    Usage ::
    
        log = logger.getDefault('my_logger')
        log.info('message')

    """
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)-12s %(levelname)-8s: %(message)s ", )        
    
    # Formatting
    formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s: %(message)s ")
    
    # The actual logger
    _logger = logging.getLogger(name)
        
    if include_syslog:
        syslog = xcLogger( name )
        syslog.setFormatter(formatter)
        _logger.addHandler(syslog)
        
    if include_console:
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        _logger.addHandler(console)

    return _logger

def xcLogger( appname ):
    """ Cross-platform log handler

        Returns:
        
        * NTEventLogHandler for win32 platform
        * SysLogHandler for Unix/Linux platforms
    """
    if (sys.platform[:3] == 'win'):
        return logging.handlers.NTEventLogHandler( appname )
    
    return logging.handlers.TimedRotatingFileHandler('/var/log/%s.log' % appname)

    #More difficult to configure as it defaults to localhost:514 
    #return logging.handlers.SysLogHandler()         

