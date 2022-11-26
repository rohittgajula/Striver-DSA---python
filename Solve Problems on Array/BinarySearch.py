
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

# method 2
# using recursion

def binarySearch(arr, low, high, target):
    arr.sort()                  # [1,2,3,5,6,8]
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr, low, mid-1, target)
        else:
            return binarySearch(arr, mid+1, high, target)
    else:
        return -1

arr = [3,5,1,6,2,8]
target = 6
BinarySearch(arr, target)
print(binarySearch(arr, 0, len(arr)-1, target))

