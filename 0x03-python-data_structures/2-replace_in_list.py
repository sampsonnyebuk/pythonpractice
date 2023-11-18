def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    my_list[idx] = element
    return my_list






my_list = [1, 2, 3, 4, 5]
idx = 3
element = 9

result = replace_in_list(my_list, idx, element)
print(result)
print(my_list)
