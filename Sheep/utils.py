def del_repeated_elem(test_list):
    aux_list = [ii for n, ii in enumerate(test_list) if ii not in test_list[:n]]
    return  aux_list


def generate_list(N):
    db = list()
    [db.append(str(i)) for i in range(0, N)]
    return db
