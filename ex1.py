def intersection(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    i = 0
    j = 0
    temp = []

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            temp.append(arr2[j])
            j += 1
            i += 1
    return temp

firstArray = [1,2,3,4,5]
secondArray = [3,5]
print(intersection(firstArray, secondArray))

