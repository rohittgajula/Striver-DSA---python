def BinarySearch(arr, target):
    n = len(arr)
    arr.sort()

    low = 0
    high = n-1
    Found = False

    while low < high and not Found:
        mid = (low + high) // 2
        if (target < arr[mid]):
            high = mid - 1
        elif (target > arr[mid]):
            low = mid + 1
        else:
            Found = True

    if Found == True:
        return "Target is found!"
    else:
        return "Target is not found!!"

arr = [3,5,1,6,9,10]
target = 11
print(BinarySearch(arr, target))

