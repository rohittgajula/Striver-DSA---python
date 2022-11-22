# USING HASHING
# method 2          Time Complexity is : O(n)
#                   Space Complexity is : O(n)

def MajorityElements(arr):      # [3,2,3,2,3]
    n = len(arr)
    m = {}          

    for i in range(n):
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1
        print(m)
    count = 0
    for key in m:
        if m[key] > n/2:
            count = 1
            print(key)
            break
    if (count == 0):
        print("No Majority Element.")


# method 1          Time Complexity is : O(n*n)
#                   Space Complexity is : O(1)

def majorityelement(arr):
    n = len(arr)

    max_count = 0
    index = 0

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count > max_count:
            max_count = count
            index = i
    if max_count > n // 2:
        print(arr[index])
    else:
        print("No Majority Element")


arr = [3,2,3,2,3]
MajorityElements(arr)
print()
majorityelement(arr)

