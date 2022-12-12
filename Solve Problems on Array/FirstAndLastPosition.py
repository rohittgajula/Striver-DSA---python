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

arr = [5,7,7,8,8,10]
target = 7
print(Position(arr, target))

