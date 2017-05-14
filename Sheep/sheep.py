from utils import del_repeated_elem, generate_list


class InputParser(object):
    def __init__(self, path_file):
        self.fd = open(path_file, "r")
        self.input_lines = []
        self.cases = int()

    def get_txt_file_info(self):
        self.input_lines = self.fd.readlines()
        self.cases = int(self.input_lines[0])
        self.input_lines.pop(0)
        return self.cases, self.input_lines

    def close_file(self):
        self.fd.close()

if __name__ == '__main__':
    file_hnd = InputParser("c-input.in")
    cases, data_set = file_hnd.get_txt_file_info()
    db = generate_list(10)

    for data in data_set:
        test_list = []
        a = []
        for test in range(1, cases+1):
            counter = test
            number = int(data) * test
            num_list = (list(str(number)))
            test_list += num_list
            clean_list = del_repeated_elem(test_list)
            last_element = clean_list[-1]
            clean_list.sort()
            if db == clean_list:
                print("Case #{} : {}".format(test, last_element))
                break

        if counter >= cases:
            print("INSMONIA")




fd.close()
