# logging is used to track events that occur in software when it runs
# it is used in debugging , testing and development 
# logging is used to track error or exception in the information 

# we have a module called logging to implement logbook

import logging 
from logging import *
mem
logging.basicConfig(level=10)
logging.debug("This is the information/debug message")
logging.info("This is the info message")
logging.warning("This is the warning message")
logging.error("There is the error in the program")
logging.critical("This is critical message and this want to be solved very quickly")