# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Method 1

def rotateArray(arr, step):
    n = len(arr)
    temp = []

    for i in range(step, n):
        temp.append(arr[i])

    for i in range(0,step):
        temp.append(arr[i])
    arr = temp.copy()               # replacing arr elements in arr with temp.
    return arr                      # we can use direct temp here

arr = [4,3,6,8,2,0]


# Method 2

def RotateArray(arr, step):
    n = len(arr)
    arr[:] = arr[step:n] + arr[0:step]
    return arr

print(rotateArray(arr, step=2))
print(RotateArray(arr, step=3))

