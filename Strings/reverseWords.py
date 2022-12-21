# method 1

def reverseString(str):

    # split the given sentence
    s = str.split()[::-1]
    l = []

    for i in s:
        l.append(i)
    return (" ".join(l))

# method 2

def revString(str):

    # split the given sentence
    words = str.split()

    # reverse the separated words and join them
    reverse_sentence = (' '.join(reversed(words)))

    return reverse_sentence


str = "How are you rohit"
print(reverseString(str))
print(revString(str))

