__author__ = "Yanina Ortiz"
__email__ = "yaninaandreaortiz@gmail.com"
__version__ = "1.0.0"


def del_repeated_elem(test_list):
    """
    Delete repeated elements in a list
    :param test_list: Initial List
    :type test_list: list()
    :return: Final list whitou repeated elements
    :rtype: list()
    """
    aux_list = [ii for n, ii in enumerate(test_list)
                if ii not in test_list[:n]]
    return aux_list


def generate_list(n):
    """
    Generates a list, which conteins a sequence of numbers
    :param n: Max number to generate
    :type n: int()
    :return: A list whit a progressive sequence of numbers
    :rtype: list()
    """
    db = list()
    [db.append(str(i)) for i in range(0, n)]
    return db


class InputParser(object):
    def __init__(self, path_file):
        self.fd = open(path_file, "r")
        self.input_lines = []
        self.cases = int()

    def get_txt_file_info(self):
        """
        Read all lines in a file
        :return: A number of cases to try, and input lines
        :rtype: tuple(int, list)
        """
        self.input_lines = self.fd.readlines()
        if self.input_lines == []:
            raise IndexError
        self.cases = int(self.input_lines[0])
        self.input_lines.pop(0)

        return self.cases, self.input_lines

    def close_file(self):
        self.fd.close()
