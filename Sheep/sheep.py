__author__ = "Yanina Ortiz"
__email__ = "yaninaandreaortiz@gmail.com"
__version__ = "1.0.0"


from utils import del_repeated_elem, generate_list, InputParser


class Sheep(object):
    def __init__(self):
        pass

    def fall_asleep(self, cases):
        """
        It determinates if the result of a count is
        sleep or insomnia
        :param cases: Max limit to coune
        :type: int
        :return: A msg whit the last number registered or insmonia
        :rtype: str()
        """
        test_list = []
        clean_list = []
        msg = str()
        for test in range(1, cases + 1):
            number = int(data) * test
            num_list = (list(str(number)))
            test_list += num_list
            clean_list = del_repeated_elem(test_list)
            last_element = clean_list[-1]
            clean_list.sort()
            if db == clean_list:
                msg = "Case #{} : {}".format(test, last_element)
                break
            elif test == cases:
                msg = "INSMONIA"
        return msg


if __name__ == '__main__':
    try:
        file_hnd = InputParser("c-input.in")
        cases, data_set = file_hnd.get_txt_file_info()
        file_hnd.close_file()
        db = generate_list(10)
        sheep = Sheep()
        for data in data_set:
            result = sheep.fall_asleep(cases)
            print(result)
    except IndexError:
        print("Input file is not long enought")
    except IOError:
        print("Input file is invalid or doesnot exist")
    except Exception as e:
        print("Unkwnoun error:{}".format(e))
