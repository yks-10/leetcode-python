class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def reverse_traversal(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=' ')
            current = current.prev
        print()

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = Node(data)
        last.next.prev = last

    def delete(self, value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            current = None
            return
        while current and current.data != value:
            current = current.next
        current.next.prev = current.prev
        current.prev.next = current.next
        current = None



l = DoubleLinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.traversal()
l.reverse_traversal()
l.delete(3)
l.traversal()
l.reverse_traversal()