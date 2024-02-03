class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, *data):
        for item in data:
            new_node = Node(item)
            if not self.head:
                self.head = new_node
            else:
                self.tail.link = new_node
                new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

    def remove(self, data):
        current = self.head
        while current and current.data != data:
            current = current.link

        if current:
            if current.prev:
                current.prev.link = current.link
            else:
                self.head = current.link
            if current.link:
                current.link.prev = current.prev
            else:
                self.tail = current.prev
            self.length -= 1
            return True
        else:
            return False

    def insert(self, index, data):
        if index < 0:
            index = self.length + index
        if index < 0 or index > self.length:
            return False
        new_node = Node(data)
        if index == 0:
            if self.head:
                new_node.link = self.head
                self.head.prev = new_node
            else:
                self.tail = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.link
            new_node.link = current.link
            if current.link:
                current.link.prev = new_node
            else:
                self.tail = new_node
            new_node.prev = current
            current.link = new_node
        self.length += 1
        return True

    def reverse(self):
        self.head, self.tail = self.tail, self.head
        current = self.head
        while current:
            current.prev, current.link = current.link, current.prev
            current = current.link

    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.data == target:
                return index
            current = current.link
            index += 1
        return -1

    def find(self, callback):
        current = self.head
        while current:
            if callback(current.data):
                return current.data
            current = current.link
        return None

    def __iter__(self):
        self._iter_node = self.head
        return self

    def __next__(self):
        if self._iter_node:
            data = self._iter_node.data
            self._iter_node = self._iter_node.link
            return data
        else:
            raise StopIteration

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.link
        return ' <-> '.join(elements)

    def __len__(self):
        return self.length
