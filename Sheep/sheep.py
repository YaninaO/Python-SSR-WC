db = list()
[db.append(str(i)) for i in range(0, 10)]

T = 100
N = 1
test_list = []
counter = 0

for test in range(1, T+1):
    counter = test
    number = N * test
    num_list = (list(str(number)))
    test_list += num_list
    a = [ii for n, ii in enumerate(test_list) if ii not in test_list[:n]]
    last = a[-1]
    a.sort()
    if db == a:
        print("Case #{} : {}".format(test, last))
        break

if counter >= 100:
    print("INSMONIA")

