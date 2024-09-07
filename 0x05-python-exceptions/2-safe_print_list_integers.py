#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    output = ""
    try:
        for i in range(x):
            try:
                output += "{:d}".format(my_list[i])
                count += 1
            except (ValueError, TypeError):
                continue
    except IndexError:
        pass
    print(output)
    return count
