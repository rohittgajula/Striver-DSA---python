# method 1          time complexity is : O(r*c)
#                   space complexity is : O(1)

def Max1s(matrix):
    m = len(matrix)
    n = len(matrix[0])

    maxCount = 0

    for i in range(m):
        count = 0
        for j in range(n):
            if matrix[i][j] == 1:
                count += 1
        if count > maxCount:
            maxCount = count
            row = i
    return row

matrix =  [[0,0,0,1],
           [0,1,1,1],
           [1,1,1,1],
           [0,0,0,0]]
print(Max1s(matrix))

