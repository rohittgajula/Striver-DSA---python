


def last(arr, low, high, target, n):
    if (high >= low):
        mid = low + (high - low) // 2
        if ((mid == n - 1 or target < arr[mid + 1]) and arr[mid] == target):
            return mid
        elif (target < arr[mid]):
            return last(arr, low, (mid - 1), target, n)
        else:
            return last(arr, (mid + 1), high, target, n)
    return -1

arr = [5,7,7,8,8,10]
n = len(arr)
target = 8

print([(first(arr, 0, n-1, target, n)), (last(arr, 0, n-1, target, n))])

