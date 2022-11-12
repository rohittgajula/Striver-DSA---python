def removeDuplicate(arr):
    n = len(arr)
    if (n == 0 or n == 1):
        return arr

    count = 0

    for i in range(0,n-1):
        if arr[i] != arr[i+1]:
            arr[count] = arr[i]
            count = count+1
    arr[count] = arr[n-1]
    print(count)

    return arr[0:count+1]

arr = [0,0,0,1,1,2,2,2,2,3,4,5,5,5,5,5,6,6]
print(removeDuplicate(arr))

