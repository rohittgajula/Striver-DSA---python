def Occurrence(arr, target):
    count = 0

    for element in arr:
        if element == target:
            count += 1
    return count


arr = [1,1,2,2,2,2,3]
target = 2
print(Occurrence(arr, target))