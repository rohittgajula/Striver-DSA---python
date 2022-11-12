def SortedOrNot(arr):
    n = len(arr)

    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return "sorted List"
        return "Unsorted List"

arr = [3,1,2,3,4,5]
print(SortedOrNot(arr))

