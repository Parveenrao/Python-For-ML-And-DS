# first we need to import logging modulde

# first thing we know before logging is logging levels
#------------------------------------------------------------

"""
1) DEBUG---> release information useful for debug process
2)INFO----> provide the information regarding that things are working as we want
3)WARNING----> used to warn something that happenend unexpectedly
4) ERROR ----> used to inform when we are in serious trouble
5) CRITICAL----> used to inform when we are in serious trouble , must be handled """

# We can represent these logging levels usin integers
""" 
Not_SET = 0
DEBUG= 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50"""

# by default logging levels is set to warning

# lets understand through an example

import logging
logging.basicConfig(filename='app.log',level=10)
logging.debug('This is debug messsage')    # to set deug level use logging.basicConfig(level = DEBUG/10)
logging.info('module 2 is completed , module 3 has been started')
logging.warning('warning message is displayed')
logging.error('Error  has been found')
logging.critical('Critical task must be completed first')

# if we want to combine all this into one file then set file_name = app.log

