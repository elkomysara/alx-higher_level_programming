#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""

import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
line_count = 0

def print_stats():
    """Prints accumulated metrics"""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()

        try:
            # Extract the file size from the last column
            file_size = int(data[-1])
            total_file_size += file_size

            # Extract the status code from the second last column
            status_code = data[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1

        except (IndexError, ValueError):
            continue

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
