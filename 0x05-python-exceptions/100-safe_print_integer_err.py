#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        exception_info = sys.exc_info()[1]
        print("Exception: {}".format(exception_info), file=sys.stderr)
        return (False)
