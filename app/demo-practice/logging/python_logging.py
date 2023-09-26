import logging
import pathlib

#create object logging object
logger = logging.getLogger(__name__)

#create the custom handler
c_handler = logging.StreamHandler()
#create the file handler
f_handler = logging.FileHandler('file.log')





