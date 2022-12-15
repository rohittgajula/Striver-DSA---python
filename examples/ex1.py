
# this function returns value of each roman number
def value(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 100
    if r == 'M':
        return 1000
    return -1

def romanToDecimal(str):
    res = 0
    i = 0
    n = len(str)

    while (i < n):

        # getting the value of symbol s[i]
        s1 = value(str[i])

        if (i + 1 < n):

            # getting the value of symbol s[i+1]
            s2 = value(str[i+1])

            # comparing both the values
            if (s1 >= s2):

                # value of current symbol iks generated
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:

                # value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 -s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return res


str = 'MCMIV'
print(romanToDecimal(str))