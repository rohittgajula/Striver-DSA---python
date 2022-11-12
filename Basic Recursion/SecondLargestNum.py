
#Given an array Arr of size N, print second largest element from an array

A = []
N = int(input("Enter size of array: "))

for i in range(N):
    c = int(input())
    A.append(c)
    print(A)

A.sort()

print("Second largest number is: ", A[-2])

#second method

myList = [99, 43, 1, 100, 7]
new_list = set (myList)

new_list.remove(largestValue(new_list))
print(new_list)
print(largestValue(new_list))

