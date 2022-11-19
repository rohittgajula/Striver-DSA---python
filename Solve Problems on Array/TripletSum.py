# method 1      time complexity is : O(n^3)
#               Space complexity is : O(1)

def TripletSum(arr, target):    #  0  1  2   3   4  5
    n = len(arr)                # [1, 4, 45, 6, 10, 8]

    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i] + arr[j] + arr[k] == target:
                    print( arr[i], arr[j], arr[k])
                    return True
    return False

# method 2      time complexity is : O(n^2)
#               Space Complexity is : O(1)

def tripletSum(arr, target):
    n = len(arr)
    arr.sort()      # [1, 4, 6, 8, 10, 45]

    for i in range(0, n):

        l = i+1
        r = n-1
        while (l < r):
            if (arr[i] + arr[l] + arr[r] == target):
                print(arr[i], arr[l], arr[r])
                return True
            elif(arr[i] + arr[l] + arr[r] < target):
                l += 1
            else:   # (arr[i] + arr[l] + arr[r] > target)
                r -= 1
    return False

# method 3          time complexity is : O(n^2)
#                   Space complexity is : O(n)

def Triplets(arr, target):
    n = len(arr)

    for i in range(0, n-1):

        s = set()
        current_sum = target - arr[i]
        for j in range(i+1, n):
            if (current_sum - arr[j] in s):
                print(arr[i], arr[j], current_sum-arr[j])
                return True
            s.add(arr[j])
    return False


arr = [1, 4, 45, 6, 10, 8]
target = 22
print(TripletSum(arr, target))
print(tripletSum(arr, target))
print(Triplets(arr, target))

