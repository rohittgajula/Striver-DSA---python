n = int(input())

for i in range(n):
    m = int(input())
    l = list(map(int, input().split()))
    c = 0
    for i in l:
        if i >= 1000:
            c+=1
    print(c)
