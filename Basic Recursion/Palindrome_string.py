# Check if the given String is Palindrome or not

def isPalindrome(s):
    if (s == s[::-1]):
        return "Is a Palindrome!!"
    else:
        return "NOt a Palindrome!!"

print(isPalindrome(str(input())))