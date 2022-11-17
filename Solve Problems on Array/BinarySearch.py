
def BinarySearch(arr, target):
    n = len(arr)
    arr.sort()

    low = 0
    high = n-1
    found = False

    while low <= high and not found:
        mid = (low + high) // 2
        if (target > arr[mid]):
            low = mid + 1
        elif (target < arr[mid]):
            high = mid - 1
        else:
            found = True

    if found == True:
        print("Key is found.")
    else:
        print("Key is not found.")

arr = [3,5,1,6,2,8]
target = 6
BinarySearch(arr, target)

