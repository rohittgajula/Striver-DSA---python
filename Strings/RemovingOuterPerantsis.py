

def removeOuterParantsis(str):

    res = ""
    count = 0

    for c in str:

        if (c == '(' and count > 0):
            res += c

        if (c == '(' ):
            count += 1

        if (c == ')' and count > 1):
            res += c

        if (c == ')'):
            count -= 1

    return res


str = "(()())(())()"
print(removeOuterParantsis(str))

