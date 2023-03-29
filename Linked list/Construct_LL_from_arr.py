class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

def arr_to_LL(arr, n):
    linkedlist = None

    for i in range(0,n):
        new_node = Node(arr[i])
        if linkedlist is None:
            linkedlist = new_node
        else:
            head = linkedlist
            while head.ref is not None:
                head = head.ref
            head.ref = new_node
    return linkedlist

def display_LL(linkedlist):
    if linkedlist is None:
        print("LinkedList is empty!!")
    else:
        while linkedlist is not None:
            print(linkedlist.data, end=" ")
            linkedlist = linkedlist.ref

arr = [1,2,3,4,5]
n = len(arr)
linkedlist = arr_to_LL(arr, n)
display_LL(linkedlist)

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

print()
arr = [6,7,4,3,7]
n = len(arr)
root = arr_to_LL2(arr, n)
display2(root)

