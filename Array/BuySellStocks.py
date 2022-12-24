# method 1      My own solution
#       Time Complexity is : O(n^2)
#       Space complexity is : O(1)

def MaxProfit1(price):
    n = len(price)

    max_Profit = []

    for i in range(n):
        for j in range(i,n):
            if price[i] < price[j]:
                profit = price[j] - price[i]
                max_Profit.append(profit)
                max_Profit.sort()

    if len(max_Profit) != 0:
        return max_Profit[-1]
    else:
        return 0

# method 2          time complexity is : O(n)
#                   space complexity is : O(1)

def MAxProfit2(price):
    n = len(price)        # [7,1,5,3,6,4]
    buy = price[0]
    maxProfit = 0

    for i in range(1,n):
        if (buy > price[i]):
            buy = price[i]
        elif (price[i] - buy > maxProfit):
            maxProfit = price[i] - buy
    return maxProfit

# method 3

def MaxProfit3(price):
    n = len(price)
    profit = 0

    for i in range(1,n):
        if price[i] > price[i-1]:
            profit += price[i] - price[i-1]
    return profit

# method 4          Using recursion

# curr_profit = price[j] – price[i] + maxProfit(start, i – 1) + maxProfit(j + 1, end)

def MaxProfit4(price, start, end):

    if (end <= start):
        return 0

    profit = 0

    for i in range(start, end, 1):
        for j in range(i+1, end+1):
            if price[j] > price[i]:
                curr_profit = price[j] - price[i] +\
                    MaxProfit4(price, start, i-1) +\
                        MaxProfit4(price, j+1, end)
                
                profit = max(profit, curr_profit)
    return profit

price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)
print(MaxProfit1(price))
print(MAxProfit2(price))
print(MaxProfit3(price))
print(MaxProfit4(price, 0, n-1))

