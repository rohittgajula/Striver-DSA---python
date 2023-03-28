class Node1:
    def __init__(self, data):
        self.data = data
        self.ref = None

def display1(root):
    while root is not None:
        print(root.data, end=" ")
        root = root.ref

def arr_to_LL1(arr, n):
    root = None
    for i in range(0,n):
        new_node = Node1(arr[i])

        if root == None:
            root = new_node
        else:
            head = root
            while head.ref is not None:
                head = head.ref
            head.ref = new_node
    return root

# using an extra function

class Node2:
    def __init__(self, data):
        self.data = data
        self.ref = None

def insert(root, item):
    new_node = Node2(item)

    if root is None:
        root = new_node
    else:
        head = root
        while head.ref is not None:
            head = head.ref
        head.ref = new_node
    return root

def display2(root):
    while root is not None:
        print(root.data, end=" ")
        root = root.ref

def arr_to_LL2(arr, n):
    root = None
    for i in range(0,n):
        root = insert(root, arr[i])
    return root


arr = [6,7,4,3,7]
n = len(arr)

root = arr_to_LL1(arr, n)
display1(root)

print()

root = arr_to_LL2(arr, n)
display2(root)