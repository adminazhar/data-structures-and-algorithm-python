my_dict = {'a': 5, 'b': 9, 'c': 2}

def max_value_key(my_dict):
    highest = 0
    keyHighest = ""
    for key,value in my_dict.items():
        if (value > highest):
            highest = value
            keyHighest = key 
    return keyHighest


print(max_value_key(my_dict))