def RemoveDuplicate(arr):
    n = len(arr)
    if (n == 0 or n == 1):
        return arr

    position = 0

    for i in range(n-1):
        if arr[i] != arr[i+1]:
            arr[position] = arr[i]
            position += 1
    arr[position] = arr[n-1]
    print(position)

    return arr[:position+1]

arr = [0,0,1,1,2,3,3]
print(RemoveDuplicate(arr))

