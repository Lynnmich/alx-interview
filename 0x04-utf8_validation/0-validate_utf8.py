#!/usr/bin/python3
"""A method that determines if a given data set
represents a valid UTF-8 encoding"""


def validUTF8(data):
    remaining_bytes = 0
    """iterate thro' each integer in the list"""
    for byte in data:
        value = byte & 255
        if remaining_bytes:
            if value >> 6 != 2:
                return False
            remaining_bytes -= 1
            continue
        while (1 << abs(7 - remaining_bytes)) & value:
            remaining_bytes += 1
        if remaining_bytes == 1 or remaining_bytes > 4:
            return False
        remaining_bytes = max(remaining_bytes - 1, 0)
    return remaining_bytes == 0
