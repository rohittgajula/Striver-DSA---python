# method 1              using extra memory or array

def moveZerosToEnd(arr):
    n = len(arr)
    temp = [0] * n
    count = 0

    for i in range(n):
        if arr[i] != 0:
            temp[count] = arr[i]
            count += 1
    return temp

# method 2              without using an extra memory or an extra array

def MoveZerosToEnd(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    return arr

arr = [0,1,0,3,12]
print(moveZerosToEnd(arr))
print(MoveZerosToEnd(arr))
