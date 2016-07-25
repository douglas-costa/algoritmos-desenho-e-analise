class Stack:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next  = None

    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def push(self, value):
        node      = self.Node(value)
        node.next = self.head
        self.head = node

        return True

    def pop(self):
        if self.empty():
            return None

        node      = self.head
        self.head = self.head.next

        return node

    def elements(self):
        node = self.head

        while node:
            yield node.value
            node = node.next

    def show(self):
        if self.empty():
            print('The stack is empty')
            return

        print(' - '.join(str(i) for i in self.elements()))