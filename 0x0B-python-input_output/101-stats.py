#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""


import sys


def print_statistics(total_size, status_codes):
    """
    Prints the computed statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary of the count of each status code.

    Returns:
        None
    """
    print("File size:", total_size)
    sorted_codes = sorted(status_codes.items())
    for code, count in sorted_codes:
        if count > 0:
            print("{}: {}".format(code, count))


def parse_line(line):
    """
    Parses a log line and extracts the file size and status code.

    Args:
        line (str): The log line to parse.

    Returns:
        tuple: A tuple of the file size (int) and the status code (int).
    """
    elements = line.split()
    return int(elements[-1]), elements[-2]


def main():
    """
    Main function to read stdin line by line and compute metrics.
    """
    total_size = 0
    status_codes = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
    }
    
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            size, status = parse_line(line)
            total_size += size
            if status in status_codes:
                status_codes[status] += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
