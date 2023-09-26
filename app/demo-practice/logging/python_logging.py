import logging
from pathlib import Path

#create object logging object
logger = logging.getLogger(__name__)

#create the custom handler
c_handler = logging.StreamHandler()
#create the file handler
f_handler = logging.FileHandler(Path('./demo-practice/logging/logs/error.log'))

#set Level of loggin of custom handler
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

#organizing formatter, for the event if it is a warning, error, etc
c_format = logging.Formatter('%(name)s - %(levelname)s -%(message)s')
#asctime = this is format for presenting the event
#name = name of the event
#levelname = level of the event
#message = Description of the event
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#We have to associate our formatter to each handler
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

#We should add handler to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning("📮 This is a warning")
logger.error("🙅🏽‍♀️ This is an error")









