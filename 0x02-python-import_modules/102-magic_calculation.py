#!/usr/bin/python3

if __name__ == "__main__":
    def magic_calculation(a, b):
        from calculation_102 import add, sub

    if a < b:
        result = add(a, b)
        for i in range(4, 6):
            result = add(result, i)
        return result
    else:
        return sub(a, b)
