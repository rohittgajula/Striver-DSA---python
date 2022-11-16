# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

def SortedOrNot(arr):
    n = len(arr)

    flag = 0
    i = 1

    while i < n:
        if arr[i] < arr[i-1]:
            flag = 1
        i += 1
    
    if (not flag):
        return "Sorted List"
    else:
        return "Unsorted list"

arr = [3,1,2,3,4,5]
print(SortedOrNot(arr))

