#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    try:
        while count < x:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            i += 1
    except IndexError:
        pass
    except ValueError:
        pass
    finally:
        print()
        return count
