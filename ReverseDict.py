my_dict = {'a': 1, 'b': 2, 'c': 3}


def reverse_dict(my_dict):
    reversed_dic = {}
    for key, value in my_dict.items():
        reversed_dic[value] = key
    return reversed_dic
print(reverse_dict(my_dict))