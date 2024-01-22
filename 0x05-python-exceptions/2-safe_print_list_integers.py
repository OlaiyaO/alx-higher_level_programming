def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    i = 0

    while i < x:
        try:
            current_element = my_list[i]
            if isinstance(current_element, int):
                print("{:d}".format(current_element), end="")
                printed_count += 1
            i += 1
        except IndexError:
            break

    print("")
    return printed_count
