__version__ = "1.0.0"
__email__ = "yaninaandreaortiz@gmail.com"
__author__ = "Yanina Ortiz"

import json


class InputParser(object):
    def __init__(self, path_file):
        """
        Init to parse input
        :param path_file: Path to json file
        :type path_file: str
        """
        self.path_file = path_file

    def read_json_file(self):
        """
        Parse a JSON file
        :return: Parsed file
        :rtype: list(dict)
        """
        with open(self.path_file) as camp_json:
            camp_data = json.load(camp_json)
        return camp_data
