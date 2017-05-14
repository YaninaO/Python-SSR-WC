db = list()
[db.append(str(i)) for i in range(0, 10)]

fd = open("c-input.in", "r")

input_lines = fd.readlines()
cases = int(input_lines[0])
input_lines.pop(0)

for data in input_lines:
    test_list = []
    a = []
    for test in range(1, cases+1):
        counter = test
        number = int(data) * test
        num_list = (list(str(number)))
        test_list += num_list
        a = [ii for n, ii in enumerate(test_list) if ii not in test_list[:n]]
        last = a[-1]
        a.sort()
        if db == a:
            print("Case #{} : {}".format(test, last))
            break

    if counter >= cases:
        print("INSMONIA")

fd.close()