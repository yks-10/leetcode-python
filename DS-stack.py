class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items)==0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop(-1)

    def peek(self):
        return self.items[-1]


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.peek())