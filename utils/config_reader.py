# Import Python's built-in module to read .ini configuration files
import configparser

# Import os module to work with file/folder paths safely
import os


# Create a reusable class to read configuration values from config.ini
class ConfigReader:

    # Constructor method runs automatically when object is created
    def __init__(self):
        # Create a ConfigParser object
        # This object knows how to read .ini files
        self.config = configparser.ConfigParser()

        # Build the full path to config/config.ini dynamically
        #
        # __file__ -> current file path (config_reader.py)
        # os.path.dirname(__file__) -> utils folder path
        # os.path.dirname(os.path.dirname(__file__)) -> project root folder path
        # Then we append: config/config.ini
        #
        # Example final path:
        # /Users/harish/saucedemo_pytest_framework/config/config.ini
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),  # Go to project root
            "config",  # config folder
            "config.ini"  # config file
        )

        # Read the config.ini file using the path created above
        self.config.read(config_path)

    # Generic method to read normal string values from config file
    # Example: base_url = https://www.saucedemo.com/
    def get(self, section, key):
        return self.config.get(section, key)

    # Method to read boolean values (true/false)
    # Example: headless = false
    # Returns Python boolean -> True or False
    def get_boolean(self, section, key):
        return self.config.getboolean(section, key)

    # Method to read integer values
    # Example: explicit_wait = 10
    # Returns Python integer -> 10
    def get_int(self, section, key):
        return self.config.getint(section, key)


# Create one reusable object of ConfigReader
# This allows us to import and use it directly in other files
# Example:
# from utils.config_reader import config
config = ConfigReader()