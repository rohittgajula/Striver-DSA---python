def SearchMatrix(matrix, target):
    rows = len(matrix)
    columns = len(matrix[0])

    top = 0             # looking for rows in this loop.
    bottom = rows - 1
    while top <= bottom:
        row = (top + bottom) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break

    if not (top <= bottom):
        return False

           # 2 + 3 // 2  ==  2
    row = (top + bottom) // 2
    l = 0
    r = columns - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False

# linear search method

def linearSearch(matrix, target):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == target):
                return (i,j)
    return (-1,-1)


matrix = [  [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]  ]
target = 31
print(SearchMatrix(matrix, target))
print(linearSearch(matrix, target))

