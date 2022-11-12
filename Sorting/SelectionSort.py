# Selection Sort Algorithm
# https://www.guru99.com/selection-sort-algorithm.html#5
# https://www.youtube.com/watch?v=nFG6pKhsUIY


""" The first item in the unsorted list is compared with all the values to the right hand side to check if it is the minimum value. if it is not the minimum value, then its position is swapped with the minimum value"""

def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        minValueIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[minValueIndex]:
                minValueIndex = j

                temp = arr[i]
                arr[i] = arr[minValueIndex]
                arr[minValueIndex] = temp
                print(arr)
            else:
                print(arr)
        print()

    return arr

arr = [5,4,3,2,1]
print("Sorted list: ", selectionSort(arr))


