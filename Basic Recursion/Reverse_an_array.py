# method 1


T=int(input())

for i in range(T):
    n=int(input())
    list1 = list(map(int,input().split()))
    
    for j in range(n-1,-1,-1):
        print(list1[j], end=' ')
    print()  #not required specifically


# method 2


for i in range(T):
    n = int(input())
    list1 = list(map(int, input().split()))
    
    for j in range(len(list1)):
        print(list1[::-1], end=' ')
        break

