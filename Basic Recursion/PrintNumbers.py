# print 1 to N numbers using recursion

def printNumber(n):
    if n > 0:
        printNumber(n-1)
        print(n, end=' ')

printNumber(n = 3)