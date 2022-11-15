
def repeatingElements(arr):
    n = len(arr)
    temp = []
    i = 0

    while i < n:
        if arr[i] == arr[i-1]:
            temp.append(arr[i])
        i += 1
    return temp

arr = [1,1,3,2,5,5,6,7,7]
print(repeatingElements(arr))

