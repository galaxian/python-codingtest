class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        self.head.next = new_node
        self.tail = new_node

    def dequeue(self):
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self.head is None

