# Given an array Arr of size N, print second largest element from an array.

def SecondLargest(arr):
    n = len(arr)
    largestValue = arr[0]
    SecondLargest = arr[0]

    for i in range(n):
        if arr[i] > largestValue:
            largestValue = arr[i]

    for i in range(n):
        if arr[i] > SecondLargest and arr[i] != largestValue:
            SecondLargest = arr[i]

    return SecondLargest

arr = [0,1,3,2,6,9,4]
print(SecondLargest(arr))