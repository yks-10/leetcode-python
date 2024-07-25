def Check(n):
    print(n)
    if n==0:
        return
    Check(n-1)
x=Check(10)

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
x=factorial(5)
print(x)

print('lambda')
y = lambda x: x*x
print(y(2))

numbers = [1,2,3,4,5]
y = map(lambda x: x*x, numbers)
print(list(y))

y = filter( lambda x: x%2==0, numbers)
print(list(y))


print('single linkedlist')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current=self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def append(self, data):
        node_data = Node(data)
        if not self.head:
            self.head = node_data
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node_data

    def delete(self, value):
        current = self.head
        previous = None
        if current and current.data == value:
            self.head = current.next
            current = None
            return
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
l.append(5)
l.append(6)
l.display()
l.delete(5)
l.display()

print('_______________________')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end='')
            current=current.next
        print()

    def reversediaplay(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=' ')
            current = current.prev
        print()

    def append(self, data):
        node_data = Node(data)
        if not self.head:
            self.head = node_data
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node_data
        node_data.prev = last

    def delete(self, value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            current = None
            return
        while current and current.data != value:
            current = current.next
        if current.next:
            current.prev.next = current.next
        if current.prev:
            current.next.prev = current.prev
        current = None



l = DoubleLinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.display()
l.reversediaplay()
# l.delete(5)
l.delete(5)
l.display()


print('-----------------------')


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(1)

    def peek(self):
        return self.items[-1]

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.peek())


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self, root_node):
        self.root = TreeNode(root_node)

    def insert_left(self, current_node, value):
        if current_node.left is None:
            current_node.left = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        if current_node.right is None:
            current_node.right = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def display(self, node):
        if node:
            self.display(node.left)
            print(node.data, end=' ')
            self.display(node.right)

bt = BinaryTree(1)  # Root node
bt.insert_left(bt.root, 2)
bt.insert_right(bt.root, 3)
bt.insert_left(bt.root.left, 4)
bt.insert_right(bt.root.left, 5)

bt.display(bt.root)  # Output wil


