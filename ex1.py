# method 1

def MissingNumber(arr):
    n = len(arr)

    expectedSum = n*(n+1)/2
    actualSum = sum(arr)

    return int(expectedSum - actualSum)

arr = [9,6,4,2,3,5,7,0,1]
print(MissingNumber(arr))

