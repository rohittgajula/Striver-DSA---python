class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LinkedList(self):
        if self.head is None:
            print("LinkedList is empty.")
        else:
            while self.head is not None:
                print(self.head.data, "->", end=" ")
                self.head = self.head.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

LL = LinkedList()
LL.add_begin(11)
LL.add_begin(27)
LL.print_LinkedList()

