# we can format the logging msg by passing the logging parameter

import logging
logging.basicConfig(filemode='w' , format= "%(name)s:%(levelname)s:%(message)s" , level=10 , filename='parveen.log')

logging.debug('Debug msg')
logging.info("Information about module")
logging.warning('warning to the system')
logging.error('Error found')
logging.critical('Critical task')

# we can create the object of logging becuse it provides more functionaltiy

logger = logging.getLogger()