#!/usr/bin/python3
"""A method that determines if a given data set
represents a valid UTF-8 encoding"""


def validUTTF8(data):
    remaining_bytes = 0
    """iterate thro' each integer in the list"""
    for byte in data:
        binary_representation = .format(byte, '08b')
        if remaining_bytes == 0:
            """count the number of leading '1' bits"""
            for bit in binary_represantation:
                if bit == '0':
                    break
                remaining_bytes += 1
                if remaining_bytes == 0:
                    continue
                """characters can have 1 to 4 bytes"""
                if remaining_bytes < 2 or remaining_bytes > 4:
                    return False
        else:
            """check if current byte starts with '10'"""
            if not(binary_representation[0] == '1'
                   and binary_representation[1] == '0'):
                return False
            remaining_bytes -= 1
    return remaining_bytes == 0
