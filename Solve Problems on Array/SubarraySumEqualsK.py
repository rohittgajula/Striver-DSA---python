# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# method 1

def SubarraySumEqualsK(arr, target):
    n = len(arr)

    if target in arr:
        ans = [arr.index(target)]
        return len(ans)
    for i in range(n):
        for j in range(n-1):
            if (arr[i]+arr[j+1]) == target:
                ans = [i,j+1]
    return len(ans)

# method 2

def subarraySumEqualsK(arr, target):
    pass

    ans, n = 0, len(arr)
    preSum = [arr[0]]
    dic = {}
    dic[0] = 1

    for i in arr[1:]:
        preSum.append(i+preSum[-1])
    for i in preSum:
        if i-target in dic:
            ans += dic[i-target]
        dic[i] = dic.get(i,0) + 1
    return ans

arr = [1,2,3]
target = 2
print(SubarraySumEqualsK(arr, target))
print(subarraySumEqualsK(arr, target))

