class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

def insert(linkedlist, item):
    new_node = Node(item)

    if linkedlist is None:
        linkedlist = new_node
    else:
        head = linkedlist
        while head.ref is not None:
            head = head.ref
        head.ref = new_node
    return linkedlist

def display_LL(linkedlist):
    while linkedlist is not None:
        print(linkedlist.data, end=" ")
        linkedlist = linkedlist.ref
    

def arr_to_LL(arr, n):
    linkedlist = None

    for i in range(0,n):
        linkedlist = insert(linkedlist, arr[i])
    return linkedlist


arr = [7,4,3,7,1,0,9]
n = len(arr)
linkedlist = arr_to_LL(arr, n)
display_LL(linkedlist)

