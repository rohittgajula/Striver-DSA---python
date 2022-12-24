# Method 1                  with using for loop

def LinearSearch(arr, k):
    n = len(arr)

    for i in range(n):
        if arr[i] == k:
            return 1
    return -1

# method 2                  without using for loop

def linearSearch(arr, k):

    if k in arr:
        return 1
    return -1

arr = [1,2,3,4,5,6]
k = 6
print(LinearSearch(arr, k))
print(linearSearch(arr, k))

