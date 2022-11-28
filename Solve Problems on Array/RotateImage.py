def RotateMatrix(matrix):
    n = len(matrix)

    for row in range(n):
        for col in range(row,n):
            matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

    for i in range(n):
        matrix[i].reverse()
    return matrix

matrix = [[5,1,9,11],
            [2,4,8,10],
            [13,3,6,7],
            [15,14,12,16]
]
print(RotateMatrix(matrix))

