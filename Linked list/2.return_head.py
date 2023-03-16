class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Print_LinkedList(self):
        if self.head is None:
            print("LinkedList is empty!")
        else:
            current = self.head
            while current is not None:
                print(current.data, "-->", end=" ")
                current = current.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        current = self.head
        if current is None:
            current = new_node
        else:
            while current.ref is not None:
                current = current.ref
            current.ref = new_node
            

LL = LinkedList()

LL.add_begin(30)
LL.add_begin(40)

LL.add_end(1000)

LL.Print_LinkedList()


