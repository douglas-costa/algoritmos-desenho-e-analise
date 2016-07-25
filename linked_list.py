class LinkedList:
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

    def previous_by_index(self, index):
        if index <= 0 or index > self.length - 1:
            return None

        counter       = 0
        previous_node = self.head

        while counter < index - 1:
            previous_node = previous_node.next
            counter       += 1

        return previous_node

    def insert(self, index, value):
        node = self.Node(value)

        if self.empty():
            self.head = node
            self.tail = node

        elif index <= 0:
            node.next = self.head
            self.head = node

        elif index >= self.length:
            self.tail.next = node
            self.tail      = node

        else:
            previous_node      = self.previous_by_index(index)
            node.next          = previous_node.next
            previous_node.next = node

        self.length += 1

    def remove(self, index):
        if self.empty():
            return False

        if self.length == 1:
            self.head = None
            self.tail = None

        elif index <= 0:
            self.head = self.head.next

        elif index >= self.length:
            previous_node      = self.previous_by_index(self.length - 1)
            previous_node.next = None
            self.tail          = previous_node

        else:
            previous_node      = self.previous_by_index(index)
            previous_node.next = previous_node.next.next

            if previous_node.next is None:
                self.tail = previous_node

        self.length -= 1

        return True

    def elements(self):
        node = self.head

        while node:
            yield node.value
            node = node.next

    def show(self):
        if self.empty():
            print('The list is empty')
            return

        return ' - '.join(str(i) for i in self.elements())