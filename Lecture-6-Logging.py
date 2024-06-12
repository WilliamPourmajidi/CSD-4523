# Import the logging module
import logging

# Set up the basic configuration for logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Log messages of different levels
logging.debug('This is a debug message')     # Detailed information, typically of interest only when diagnosing problems
logging.info('This is an info message')      # Confirmation that things are working as expected
logging.warning('This is a warning message') # An indication that something unexpected happened, or indicative of some problem in the near future
logging.error('This is an error message')    # Due to a more serious problem, the software has not been able to perform some function
logging.critical('This is a critical message') # A very serious error, indicating that the program itself may be unable to continue running
