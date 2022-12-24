# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

def SingleNumber(arr):
    n = len(arr)
    
    counts = {}

    for n in arr:
        if n not in counts:
            counts[n] = 1       # inserting n value in counts 4:1. 1 is any value.
            print(counts)       # to print dictionary
        else:
            del counts[n]
            print(counts)       # to print dictionary
    return list(counts.keys())

arr = [4,1,2,1,2]
print(SingleNumber(arr))

