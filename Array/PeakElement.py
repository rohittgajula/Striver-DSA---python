def PeakElement(arr, low, high, n):

    mid = (low + high) // 2

    if (mid == 0 or arr[mid-1] <= arr[mid]) and (mid == n-1 or arr[mid+1] <= arr[mid]):
        return mid
    elif (mid > 0 and arr[mid-1] > arr[mid]):
        return PeakElement(arr, low, mid-1, n)
    else:
        return PeakElement(arr, mid+1, high, n)


arr = [1,2,1,3,5,6,4]
n = len(arr)
print(PeakElement(arr, 0, n-1, n))
