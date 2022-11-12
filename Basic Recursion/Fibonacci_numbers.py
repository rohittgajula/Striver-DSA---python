# using loops                   loops is faster than recursion

def fibonacci(n):
    ar = [0] * n
    ar[0] = 1

    if n == 1:
        return ar

    ar[1] = 1
    for i in range(2,n):
        ar[i] = ar[i-2] + ar[i-1]
    return ar

print(fibonacci(n=54))

# using recursion              recursion is slower than loops

def fibonacci(n):
    if (n<=1):
        return n
    
    Last = fibonacci(n-1)
    SecondLast = fibonacci(n-2)
    return Last + SecondLast


print(fibonacci(n=54))