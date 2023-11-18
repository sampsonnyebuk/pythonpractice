# Write a function that replaces all occurrences of an element by another in a new list.

# Prototype: def search_replace(my_list, search, replace):
# my_list is the initial list
# search is the element to replace in the list
# replace is the new element
# You are not allowed to import any module


# guillaume@ubuntu:~/0x04$ cat 1-main.py
# #!/usr/bin/python3
# search_replace = __import__('1-search_replace').search_replace

# my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
# new_list = search_replace(my_list, 2, 89)

# print(new_list)
# print(my_list)

# guillaume@ubuntu:~/0x04$ ./1-main.py
# [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
# [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
# guillaume@ubuntu:~/0x04$

def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)

    return new_list



my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
