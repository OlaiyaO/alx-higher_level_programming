#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, number in enumerate(row):
            print("{:d}".format(number), end="")
            if i != len(row) - 1:
                print(" ", end="")
        print()
