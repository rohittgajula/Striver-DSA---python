def unionArray(arr1, arr2):
    m = len(arr1)  # m=4
    n = len(arr2)  # n=3

    i = 0
    j = 0
    temp = []
    temp1 = []          # for intersection

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            temp.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            temp.append(arr2[j])
            j += 1
        else:
            temp.append(arr2[j])
            temp1.append(arr2[j])   # for intersection
            i += 1
            j += 1
        print(temp, i, j)       # for step by step process
    print()

    while i < m:
        temp.append(arr1[i])
        i += 1
    while j < n:
        temp.append(arr2[j])
        j += 1

    print(str(temp) + " is the union of two arrays")
    print(str(temp1) + " is the intersection of two arrays")

firstArray = [1,2,4,5]
secondArray = [2,3,6]
unionArray(firstArray, secondArray)

