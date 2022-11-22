

def get_product_array(arr):
    n = len(arr)
    left  = [1] * n
    right = [1] * n
    product_array = []

    # build left hand array
    for i in range(1,n):
        left[i] = left[i-1] * arr[i - 1]
        print(left)
    print()

    # build right hand array
    for i in range(1,n):
        right[i] = right[i-1] * arr[::-1][i-1]
        print(right)
    print()

    # build product array from subarray
    for i in range(n):
        product_array.append(left[i] * right[::-1][i])

    return product_array

arr = [1,2,3,4]
print(get_product_array(arr))

