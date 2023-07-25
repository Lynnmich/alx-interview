#!/usr/bin/python3
"""
Print Pascal's Triangle
"""


def pascal_triangle(n):
    """Returns Pascal's triangle in a list of a list"""
    my_list = []
    if (n <= 0):
        return my_list
    my_list.append([1])
    for i in range(n - 1):
        my_list.append([1] + [my_list[i][j] + my_list[i][j + 1]
                              for j in range(len(my_list[i]) - 1)] + [1])
    return my_list
