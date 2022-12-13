# method 1
# time complexity is : O(n)

def Position(arr, target):
    n = len(arr)

    first = -1
    last = -1

    for i in range(n):
        if (target != arr[i]):
            continue
        if (first == -1):
            first = i
        last = i
    return (first, last)

# method 2
# time complexity is : O(log N)

def BinSearch(arr, target, leftBias):
    l = 0
    r = len(arr) - 1
    i = -1
 
    while l <= r:
        m = (l+r)//2
        if target > arr[m]:
            l = m+1
        elif target < arr[m]:
            r = m-1
        else:
            i = m
            if leftBias:
                r = m-1
            else:
                l = m+1
    return i

# ------------------------------

arr = [5,7,7,8,8,10]
target = 8
print(Position(arr, target))

left = BinSearch(arr, target, True)
right = BinSearch(arr, target, False)
print([left, right])
