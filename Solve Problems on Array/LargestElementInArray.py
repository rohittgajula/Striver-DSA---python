# Given an array A[] of size n. The task is to find the largest element in it.

def Largest(arr):
    n = len(arr)
    max = arr[0]   # here max value is 1 as arr[0] = 1

    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [1,8,7,56,90,65]
print(Largest(arr))

