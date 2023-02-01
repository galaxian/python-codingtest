from 자료구조.linkedlist import Node


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peak(self):
        return self.head.data
