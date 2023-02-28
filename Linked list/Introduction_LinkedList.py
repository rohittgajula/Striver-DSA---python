# How to create a node
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
                print(n.data, "--->")
                n = n.ref

    # How to add the element at the beginning
    # https://www.youtube.com/watch?v=B-zO18TJKYQ
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # how to add the element at the ending
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

# for traverse operation
LL1 = LinkedList()


# for adding in the beginning operation
LL1.add_begin(27)
LL1.add_begin(9)

# for adding in the ending operation
LL1.add_end(100)


# for traverse operation/continuation to line-42
LL1.print_LL()