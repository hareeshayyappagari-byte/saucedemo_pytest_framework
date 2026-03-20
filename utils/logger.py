# Import Python's built-in logging module
# This module is used to create and manage logs
import logging

# Import os module to work with file paths and folders
import os


# Create a reusable function that returns a configured logger object
# name="test_logger" means if no name is passed, default logger name will be "test_logger"
def get_logger(name="test_logger"):

    # Build the path for the logs folder dynamically
    #
    # __file__ -> current file path (utils/logger.py)
    # os.path.dirname(__file__) -> utils folder path
    # os.path.dirname(os.path.dirname(__file__)) -> project root folder path
    # Then append "logs"
    #
    # Final example:
    # /Users/harish/saucedemo_pytest_framework/logs
    logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")

    # Create logs folder if it doesn't already exist
    # exist_ok=True prevents error if folder is already present
    os.makedirs(logs_dir, exist_ok=True)

    # Create or get a logger object with the given name
    # If logger already exists with this name, Python returns the same logger
    logger = logging.getLogger(name)

    # Set minimum logging level
    # INFO means logger will capture:
    # INFO, WARNING, ERROR, CRITICAL
    logger.setLevel(logging.INFO)

    # Prevent adding handlers multiple times
    # If handlers are added again and again, duplicate log messages may appear
    if not logger.handlers:

        # FileHandler writes logs into a file
        # File will be created inside logs folder as automation.log
        file_handler = logging.FileHandler(os.path.join(logs_dir, "automation.log"))

        # StreamHandler prints logs in terminal / console
        console_handler = logging.StreamHandler()

        # Define the format of each log line
        #
        # %(asctime)s  -> date and time of log
        # %(levelname)s -> INFO / ERROR / WARNING etc.
        # %(name)s -> logger name
        # %(message)s -> actual log message
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        # Apply the formatter to file handler
        # So file logs will follow the above format
        file_handler.setFormatter(formatter)

        # Apply the same formatter to console handler
        # So terminal logs also look same
        console_handler.setFormatter(formatter)

        # Attach file handler to logger
        # This means logs will be written to automation.log file
        logger.addHandler(file_handler)

        # Attach console handler to logger
        # This means logs will also print in terminal
        logger.addHandler(console_handler)

    # Return the fully configured logger object
    return logger