# Insertion Sort
# https://www.youtube.com/watch?v=ltqbC8x9lWg&t=308s

"""Insertion sort is a simple algorithm that works the way we sort playing cards in our hand."""


def insertionSort(arr):
    n = len(arr)

    for index in range(1,n):
        currentElement = arr[index]
        pos = index
        while currentElement < arr[pos-1] and pos > 0:
            arr[pos] = arr[pos-1]
            pos = pos-1
        arr[pos] = currentElement
        print(arr)
    print()
    return arr

arr = [3,5,1,2,9,0]
print(insertionSort(arr))

