

def SingleElement(arr):
    arr.sort()
    n = len(arr)

    ans = 0

    for i in range(0,n,2):
        if(arr[i] != arr[i+1]):
            ans = arr[i]
            break
    if (arr[n-2] != arr[n-1]):
        ans = arr[n-1]

    return ans


arr = [1,1,2,3,3,4,4,8,8]
print(SingleElement(arr))

