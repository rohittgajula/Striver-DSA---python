def Largest(arr):
    n = len(arr)
    max = arr[0]

    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [1,8,7,56,90,65]
print(Largest(arr))
