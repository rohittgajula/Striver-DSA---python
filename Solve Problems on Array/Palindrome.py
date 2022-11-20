def Palindrome(str):
    newStr = ""

    for c in str:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]


str = "A man, a plan, a canal: Panama"
print(Palindrome(str))