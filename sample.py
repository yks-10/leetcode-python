class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = Node(data)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current =current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        current = prev
        while current:
            print(current.data, end=' ')
            current = current.next
        print()
l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.display()
l.reverse()