def TripletSum(arr, target):
    n = len(arr)

    for i in range(0, n):
        for j in range(i+1, n-1):
            for k in range(j+1, n-1):
                if arr[i] + arr[j] + arr[k] == target:
                    print(arr[i], arr[j], arr[k])
                    return True
    return False

arr = [4,2,3,7,1,0,6]
target = 7
print(TripletSum(arr, target))

