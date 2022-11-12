def RemoveDuplicate(arr):
    n = len(arr)
    if (n == 0 or n == 1):
        return arr

    count = 0

    for i in range(n-1):
        if arr[i] != arr[i+1]:
            arr[count] = arr[i]
            count += 1
    arr[count] = arr[n-1]

    return arr[0:count+1]


arr = [0,0,1,1,2,3,3]
print(RemoveDuplicate(arr))

