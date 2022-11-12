# counting the frequency of an element

from operator import index


a = list(map(int, input().split()))

count = {}

for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

print(count)
