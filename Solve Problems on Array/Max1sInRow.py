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

# method 2

def first(arr, low, high):

    if high >= low:
        mid = low + (high - low) // 2
        if (mid == 0 or arr[mid-1] == 0 and arr[mid] == 1):
            return mid
        elif arr[mid] == 0:
            return first(arr, (mid + 1), high)
        else:
            return first(arr, low, (mid - 1))
    return -1

def rowWithMin1s(matrix):

    r = len(matrix)
    c = len(matrix[0])
    max_row_index = 0
    max = -1
    for i in range(0, r):
        index = first(matrix[i], 0, c-1)
        if index != -1 and c - index > max:
            max = c - index
            max_row_index = i
    return max_row_index

matrix =  [[0,0,0,1],
           [0,1,1,1],
           [1,1,1,1],
           [0,0,0,0]]
print(Max1s(matrix))
print(rowWithMin1s(matrix))

