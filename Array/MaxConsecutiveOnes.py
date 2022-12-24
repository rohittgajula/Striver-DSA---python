# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def MaxConsecutiveOnes(arr):
    n = len(arr)
    count = 0
    result = 0

    for i in range(n):
        if (arr[i] == 0):
            count = 0
        else:
            count += 1
            print(result, end=' ')
            result = max(result, count)
    print()

    return result

arr = [1,1,0,1,1,1]
print(MaxConsecutiveOnes(arr))

