# method 1
# time complexity is : O(n)

def Rearrange(arr):
    n = len(arr)

    positive_array = []
    negative_array = []
    ans = []

    for i in arr:
        if i > 0:
            positive_array.append(i)
        else:
            negative_array.append(i)

    for i in range(int(n/2)):
        ans.append(positive_array[i])
        ans.append(negative_array[i])
    return ans

# method 2

def ReArrange(arr):
    n = len(arr)
    ans = [None] * n

    ans[::2] = (x for x in arr if x > 0)
    ans[1::2] = (x for x in arr if x < 0)
    return ans

arr = [3,1,-2,-5,2,-4]
print(Rearrange(arr))
print(ReArrange(arr))
