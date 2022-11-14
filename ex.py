def UnionArray(arr1, arr2):
    m = len(arr1)   # = 5
    n = len(arr2)   # = 3

    i = 0
    j = 0
    temp = []
    temp1 = []                 # temp1 is for insertion

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            temp.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            temp.append(arr2[j])
            j += 1
        else:
            temp.append(arr2[j])
            temp1.append(arr2[j])         # for intersection
            j += 1
            i += 1
    print(temp, i, j)

    while i < m:
        temp.append(arr1[i])
        i += 1
    while j < n:
        temp.append(arr2[j])
        j += 1
    
    print(str(temp) + " is union of two arrays") 
    print(str(temp1) + " is intersection of two arrays")

firstArray = [1,2,4,5,6]
secondArray = [2,3,5]
UnionArray(firstArray, secondArray)


