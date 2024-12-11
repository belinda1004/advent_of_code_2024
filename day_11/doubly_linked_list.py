class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, after_node, value):
        new_node = Node(value)
        new_node.prev = after_node
        new_node.next = after_node.next

        if after_node.next:
            after_node.next.prev = new_node
        else:
            self.tail = new_node

        after_node.next = new_node
        self.length += 1


    def display(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")