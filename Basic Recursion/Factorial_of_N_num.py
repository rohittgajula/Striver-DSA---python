# python program to find factorial of N numbers using recursion

n = int(input())

def fact(n):
    if n == 0:
        return 1
    else:
        return (n*(fact(n-1)))

print(fact(n))