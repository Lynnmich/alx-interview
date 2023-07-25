def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # the first row

    for row in range(1, n):
        current_row = [1]  # the first element of each row is 1

        for position in range(1, len(triangle[row-1])):
            value = triangle[row-1][position] + triangle[row-1][position-1]
            current_row.append(value)

        current_row.append(1)  # the last element of each row is 1
        triangle.append(current_row)

    return triangle
~                        
