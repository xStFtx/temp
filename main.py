class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None  # Renamed from 'link' to 'next' for clarity

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, *data):
        for item in data:
            self.insert(self.length, item)

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.length -= 1
                return True
            current = current.next
        return False

    def insert(self, index, data):
        if index < 0:
            index += self.length
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")

        new_node = Node(data)
        if index == 0:
            if not self.head:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node

        self.length += 1

    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1

    def find(self, callback):
        current = self.head
        while current:
            if callback(current.data):
                return current.data
            current = current.next
        return None

    def __iter__(self):
        self._iter_node = self.head
        return self

    def __next__(self):
        if self._iter_node:
            data = self._iter_node.data
            self._iter_node = self._iter_node.next
            return data
        else:
            raise StopIteration

    def __str__(self):
        return " <-> ".join(str(node.data) for node in self)

    def __repr__(self):
        return f"LinkedList([{', '.join(repr(node.data) for node in self)}])"

    def __len__(self):
        return self.length
