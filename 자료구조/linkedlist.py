class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        cnt = 0
        while cnt < index:
            node = node.next
            cnt += 1
        return node


Llist = LinkedList(0)
Llist.append(1)
Llist.append(2)
Llist.print_all()
print(Llist.get_node(1))




