# Using Kadane's algorithm
#   Time Complexity is : O(n)

def MaxSubarray(arr):
    n = len(arr)
    maxSub = arr[0]
    curSum = 0

    for i in arr:
        if curSum < 0:
            curSum = 0
        curSum += i
        maxSub = max(maxSub, curSum)
    return maxSub


arr = [-2,1,-3,4,-1,2,1,-5,4]
print(MaxSubarray(arr))

