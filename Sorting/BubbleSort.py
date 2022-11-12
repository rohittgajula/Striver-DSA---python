# https://www.youtube.com/watch?v=GPv7gNRR9W4

"""it is a sorting algorithm used to sort list items in ascending order to comparing two adjacent values, if the first value is higher than the second value, the first value takes the second position, while second value takes the first value position. if the first value is lower than the second value, than no swapping is done."""

def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1-i):      # -i is used to delete sorted list. we can delete -i also
            if arr[j] > arr[j+1]:

                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                print(arr)          # to show iteration
            else:                   # to show not satisfied iteration also
                print(arr)
        print()

    return arr

arr = [3,6,1,-4,0]
print("sorted list: ", bubbleSort(arr))
