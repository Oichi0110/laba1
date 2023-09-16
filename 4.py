def max_three_values(my_dict):
    values = list(my_dict.values())
    values.sort()
    size = len(values)
    values_list = values[size - 3: size]
    key_list = []
    for i in range(0, 3):
        elem = list(my_dict.keys())[list(my_dict.values()).index(values_list[i])]
        if elem in key_list:
            my_dict.pop(elem, None)
            elem = list(my_dict.keys())[list(my_dict.values()).index(values_list[i])]
            key_list.append(elem)
        else:
            key_list.append(elem)
    print(key_list)


max_three_values({'a': 504560, 'b': 5874, 'c': 5875645, 'd': 44600, 'e': 5874, 'f': 20})
max_three_values({'c': 46456, 'a': 5874, 's': 5360456, 'x': 12320, 'e': 45874, 'f': 12320})
