# import logging

#order by severity, low to high
# logging.debug("this is debug")
# logging.info("this is info")
# logging.warning("this is warning")
# logging.error("this is error")
# logging.critical("this is critical")


###---------------------------------------------------
## Example 2
## Notes:CamelCasing goes against PEP 8 standard
## Link info: <>
###---------------------------------------------------

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("🥶 This will get logged")

###---------------------------------------------------
## Example 3
## Notes:CamelCasing goes against PEP 8 standard
## Link info: <>
###---------------------------------------------------

import logging

# ## loggoing.basicConfig can only be called once
# logging.basicConfig(
#   filename='./demo-practice/logging/ynab_app.log', #name of the log file
#   filemode='w',             #file mode is to "w" (write), "r" (read)
#   format='%(name)s - %(levelname)s - %(message)s'
# )
# logging.debug("🐞 This will get logged")
# logging.warning("☢️ This will get logged")
# logging.error("😖 This will get logged")

###---------------------------------------------------
## Example 4
## Notes:CamelCasing goes against PEP 8 standard
## Link info: <>
###---------------------------------------------------

# This is done to log events
# import logging

# logging.basicConfig(
#   filename='./demo-practice/logging/ynab_appv2.log', #name of the log file
#   format='%(asctime)s - %(message)s',
#   datefmt='%d-%b-%y %H:%M:%S'
# )
# logging.warning("☢️ Admin logged out")
# logging.error("😖 This will get logged")

###---------------------------------------------------
## Example 5
## Notes:CamelCasing goes against PEP 8 standard
## Link info: <>
###---------------------------------------------------
import logging

logging.basicConfig(
  filename='./demo-practice/logging/ynab_appv3.log', #name of the log file
  format='%(asctime)s - %(message)s',
  datefmt='%d-%b-%y %H:%M:%S'
)

try:
  result = 3/0
except Exception as e:
  logging.warning("☢️ There is something wrong with the dividend")
  #logging.error("😖 Division is not correct",exc_info=True)
  logging.exception("😰 Exception was caught")

