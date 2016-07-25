class Queue:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next  = None

    def __init__(self):
        self.length = 0
        self.head   = None
        self.tail   = None

    def empty(self):
        return self.length == 0

    def enqueue(self, value):
        node = self.Node(value)

        if self.empty():
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail      = node

        self.length += 1

        return True

    def dequeue(self):
        if self.empty():
            return None

        node        = self.head
        self.head   = self.head.next
        self.length -= 1

        return node

    def elements(self):
        node = self.head

        while node:
            yield node.value
            node = node.next

    def show(self):
        if self.empty():
            print('The queue is empty')
            return

        print(' - '.join(str(i) for i in self.elements()))