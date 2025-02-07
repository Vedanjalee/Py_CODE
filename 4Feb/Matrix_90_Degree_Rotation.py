def rotate_matrix_90_clockwise(matrix):
    
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    
    for row in matrix:
        row.reverse()

    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_matrix_90_clockwise(matrix)
for row in rotated_matrix:
    print(row)
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]