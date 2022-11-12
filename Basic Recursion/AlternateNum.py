#Print alternate elements of an array

#You are given an array A of size N. You need to print elements of A in alternate order (starting from index 0).

a = []
n = int(input(" Enter number of test cases: "))
b = []

for i in range(n):
    c=int(input())
    a.append(c)

for j in range(0,n,2):
    b.append(a[j])

print(b)


# recursion method

def printAlter(arr):
    n = len(arr)

    for i in range(n):
        if (i % 2 == 0):
            print(arr[i], end=' ')


arr = [1,2,3,4,5,6,7,8]
printAlter(arr)

