def SingleNumber(arr):
    n = len(arr)
    
    counts = {}

    for n in arr:
        if n not in counts:
            counts[n] = 1       # inserting n value in counts 4:1. 1 is any value.
            print(counts)
        else:
            del counts[n]
    return list(counts.keys())[0]

arr = [4,1,2,1,2]
print(SingleNumber(arr))

