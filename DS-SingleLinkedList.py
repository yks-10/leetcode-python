class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = Node(data)

    def delete(self, value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            current = None
        previous = None
        while current and current.data != value:
            previous = current
            current = current.next
        previous.next = current.next
        current = None



l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.traversal()
l.delete(3)
l.traversal()


