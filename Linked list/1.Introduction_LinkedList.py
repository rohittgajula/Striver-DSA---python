# How to create a node
# https://www.youtube.com/watch?v=xRTdfZsAz6Y
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

# How to create a Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # How to traverse operation a Linked List
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty..")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref

    # How to add node at the beginning
    # https://www.youtube.com/watch?v=B-zO18TJKYQ
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # how to add node at the ending
    # https://www.youtube.com/watch?v=o8tWJCFWEPU
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # how to add after the given node in a linked list
    # https://www.youtube.com/watch?v=enRNwavYa9U
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in LinkedList.")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # how to add before the given node in a linked list
    # https://www.youtube.com/watch?v=8-liQuPp34A
    def add_before(self, data, x):
        # only for adding node before the first node
        if self.head is None:
            print("LinkedList is empty.")
            return
        if self.head.data == x:             # same add_begin code
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        # 1.we need to identify previous node.
        # 2.go to that previous node.
        # 3.then same as adding node after a given node.
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found.")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

# for traverse operation
LL1 = LinkedList()

# for adding in the beginning operation
LL1.add_begin(27)
LL1.add_begin(9)

# for adding in the ending operation
LL1.add_end(100)

# for adding after the given node
LL1.add_after(270, 100)

# for adding before the given node
LL1.add_before(500, 270)

# for traverse operation/continuation to line-42
LL1.print_LL()