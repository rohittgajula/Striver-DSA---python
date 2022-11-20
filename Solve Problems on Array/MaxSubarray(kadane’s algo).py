# Using Kadane's algorithm
#   Time Complexity is : O(n)

def MaxSubarray(arr):
    maxSub = arr[0]
    curSum = 0

    for i in arr:
        if curSum < 0:
            curSum = 0
        curSum += i
        maxSub = max(maxSub, curSum)
    return maxSub

# method 2          Using DP method
# Time Complexity is less in this.``

def maxSubarray(arr):
    n = len(arr)
    tempArr = []
    tempArr.append(arr[0])
    curSum = arr[0]
    for i in range(1,n):
        curSum = max(curSum + arr[i], arr[i])
        tempArr.append(curSum)
    tempArr.sort()
    return tempArr[-1]

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(MaxSubarray(arr))
print(maxSubarray(arr))

