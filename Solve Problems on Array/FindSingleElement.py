

def SingleElement(arr, n):

    ans = 0

    for i in range(0,n-1,2):
        if (arr[i] != arr[i+1]):
            ans = arr[i]
            break
    if (arr[n-2] != arr[n-1]):
        ans = arr[n-1]
    return ans

arr = [1,1,3,3,4,4,8]
n = len(arr)
print(SingleElement(arr, n))

