class Dequeue:
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

    def previous(self, current_node):
        previous_node = self.head

        while previous_node != None and previous_node.next != current_node:
            previous_node = previous_node.next

        return previous_node

    def push(self, value):
        node = self.Node(value)

        if self.empty():
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail      = node

        self.length += 1

        return True

    def unshift(self, value):
        node = self.Node(value)

        if self.empty():
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head = node

        self.length += 1

        return True

    def pop(self):
        if self.empty():
            return None

        node_to_pop = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            previous_node      = self.previous(self.tail)
            previous_node.next = None
            self.tail          = previous_node

        self.length -= 1

        return node_to_pop

    def shift(self):
        if self.empty():
            return None

        node_to_pop = self.head

        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next

        self.length -= 1

        return node_to_pop

    def elements(self):
        node = self.head

        while node:
            yield node.value
            node = node.next

    def show(self):
        if self.empty():
            print('The dequeue is empty')
            return

        print(' - '.join(str(i) for i in self.elements()))