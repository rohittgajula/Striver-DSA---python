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

