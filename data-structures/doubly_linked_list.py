class DoublyLinkedList:
    class Node:
        def __init__(self, value):
            self.value    = value
            self.previous = None
            self.next     = None

    def __init__(self):
        self.length = 0
        self.head   = None
        self.tail   = None

    def empty(self):
        return self.length == 0

    def get_node(self, index):
        counter = 0
        node    = self.head

        while node != None and counter != index:
            node    = node.next
            counter += 1

        return node

    def insert(self, index, value):
        node = self.Node(value)

        if self.empty():
            self.head = node
            self.tail = node

        elif index <= 0:
            node.next          = self.head
            self.head.previous = node
            self.head          = node

        elif index >= self.length:
            node.previous  = self.tail
            self.tail.next = node
            self.tail      = node

        else:
            current_node          = self.get_node(index)
            previous_node         = current_node.previous
            node.previous         = previous_node
            node.next             = current_node
            current_node.previous = node
            previous_node.next    = node

        self.length += 1

        return True

    def remove(self, index):
        if self.empty():
            return False

        if self.length == 1:
            self.head = None
            self.tail = None

        elif index <= 0:
            self.head          = self.head.next
            self.head.previous = None

        elif index >= self.length:
            previous_node      = self.tail.previous
            previous_node.next = None
            self.tail          = previous_node

        else:
            current_node  = self.get_node(index)
            previous_node = current_node.previous
            next_node     = current_node.next

            previous_node.next = next_node

            if next_node != None:
                next_node.previous = previous_node
            else:
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

        print(' - '.join(str(i) for i in self.elements()))

    def elements_reverse(self):
        node = self.tail

        while node:
            yield node.value
            node = node.previous

    def show_reverse(self):
        if self.empty():
            print('The list is empty')
            return

        print(' - '.join(str(i) for i in self.elements_reverse()))