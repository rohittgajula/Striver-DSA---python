# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# method 1

def MissingNumber(arr):
    n = len(arr)
    temp = [0]*(n+1)
    ans = 0
    arr.sort()

    for i in range(n):              # [0,1,3,4,5]
        temp[arr[i]-1] = 1
        print(temp, i)

    for i in range(0, n+1):
        if temp[i] == 0:
            ans = i+1

    return ans

# method 2                  sometimes its wrong

def missingNumber(arr):
    n = len(arr)

    expectedSum = n*(n+1)/2
    actualSum = sum(arr)

    return abs(int(expectedSum - actualSum))

arr = [0,1,3,4,5]
print(MissingNumber(arr))
print()
print(missingNumber(arr))

