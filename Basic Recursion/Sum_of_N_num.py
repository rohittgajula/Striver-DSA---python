#Python program to find the sum of first n natural numbers tutorial

n = int(input())
i = 1
sum = 0

while(i<=n):
    sum+=i
    i+=1
print(sum)

#method 2

sum1 = (n*(n+1))/2
print(int(sum1))

# method 3 using recursion

def sum(n):
    if n == 0:
        return 0
    else:
        return (n+(sum(n-1)))

print(sum(n))