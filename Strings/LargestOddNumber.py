# runtime : O(n)

def LargestOddNumber(num):

    n = len(num)

    for i in range(n-1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i+1]
    else:
        return ""

# method 2

def largestOddNumber(num):
    number = int(num)
    l = str(number)[::-1]
    a = None
    print(l)

    for i in l:
        if int(i) % 2 != 0:
            a = int(l.index(i))
            break
    if a is None:
        return ""
    else:
        l = l[a:]
        return l[::-1]

num = "52"
print(LargestOddNumber(num))
print()
print(largestOddNumber(num))
