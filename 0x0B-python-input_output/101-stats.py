#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""


import sys


def print_stats(total_size, status_codes):
    """
    Print statistics of lines for each status code.

    Args:
        total_size (int): Total size of the files processed.
        status_codes (dict): Dictionary containing counts for each status.
    """
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(status_code, count))


def main():
    """
    Read input from stdin line by line, compute metrics, and print statistics.

    Prints statistics 10 lines or after a keyboard interruption (CTRL + C).
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

    lines_processed = 0

    try:
        for line in sys.stdin:
            try:
                data = line.split()
                size = int(data[-1])
                status_code = data[-2]

                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += size
                lines_processed += 1

                if lines_processed % 10 == 0:
                    print_stats(total_size, status_codes)
            except Exception as e:
                pass

    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
