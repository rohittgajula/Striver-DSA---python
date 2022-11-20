# method 1      My own solution
#       Time Complexity is : O(n^2)

def Stocks(arr):
    n = len(arr)

    maxProfit = []

    for i in range(n):
        for j in range(i,n):
            if arr[i] < arr[j]:
                profit = arr[j] - arr[i]
                maxProfit.append(profit)
                maxProfit.sort()

    if len(maxProfit) != 0:
        return maxProfit[-1]
    else:
        return 0

# method 2

def stocks(arr):
    n = len(arr)        # [7,1,5,3,6,4]
    buy = arr[0]
    maxProfit = 0

    for i in range(1,n):
        if (buy > arr[i]):
            buy = arr[i]
        elif (arr[i] - buy > maxProfit):
            maxProfit = arr[i] - buy
    return maxProfit

arr = [7,1,5,3,6,4]
print(Stocks(arr))
print(stocks(arr))

