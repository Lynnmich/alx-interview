#!/usr/bin/python
"""A script that reads stdin line by line and computes metrics"""


import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0


def print_n(total_size):
    """Prints the statistics"""
    print("file size: {}".format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print("{}: {}".format(key, value))


try:
    for line in sys.stdin:
        rline = line.split(" ")
        if len(rline) > 4:
            code = rline[-2]
            if code in cache.keys():
                cache[code] += 1
            filesize = int(rline[-1])
            total_size += filesize
            counter += 1
        if counter == 10:
            counter = 0
            print_n(total_size)
except Exception as ex:
    pass
finally:
    print_n(total_size)