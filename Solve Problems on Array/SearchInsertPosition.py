# method 1
# using binary search

def position(arr, target):
    arr.append(float('inf'))
    n = len(arr)
    l = 0
    r = n-1

    while(l<r):
        mid = (l+r)//2

        if target <= arr[mid]:
            r = mid
        else:
            l = mid + 1
    return l

# method 2

def Position(arr, target):
    arr.append(float('inf'))
    n = len(arr)

    for i in range(n):
        if arr[i] == target:
            return i

    if (target not in arr):
        for j in range(n):
            if target <= arr[j]:
                return j
        return n


arr = [1,3,5,6,8]
target = 10
print(position(arr, target))
print(Position(arr, target))