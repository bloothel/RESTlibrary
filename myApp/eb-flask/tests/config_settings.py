import ConfigParser
import os


class ConfigSettings:
    def __init__(self, configpath):
        self.config_path = configpath
        if not os.path.isfile(self.config_path):
            raise Exception("File not found: %s " % self.config_path)
        self.Config = ConfigParser.ConfigParser()
        self.Config.read(self.config_path)

    def get(self, section_name, param_name):
        """
        Returns specific parameter in section
        :rtype : str, str
        """
        try:
            return self.Config.get(section_name, param_name)
        except ConfigParser.NoOptionError:
            return False

    def get_section(self, section_name):
        """
        Returns entire section of config
        :rtype : dict
        """
        try:
            return self.Config.items(section_name)
        except ConfigParser.NoOptionError:
            return False
