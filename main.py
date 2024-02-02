class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # For doubly linked list
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Keeping track of tail for efficient additions

    def add(self, *data):
        for item in data:
            new_node = Node(item)
            if not self.head:
                self.head = new_node
            else:
                self.tail.link = new_node
                new_node.prev = self.tail
            self.tail = new_node

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
            return True
        else:
            return False

    def insert(self, index, data):
        if index < 0:
            return False  # Negative index not allowed
        new_node = Node(data)
        if index == 0:
            if self.head:
                new_node.link = self.head
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    return False  # Index out of bounds
                current = current.link
            new_node.link = current.link
            if current.link:
                current.link.prev = new_node
            new_node.prev = current
            current.link = new_node
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
        return ' <-> '.join(elements)  # Changed to <-> to indicate bidirectional links

# Example usage
ll = LinkedList()
ll.add(1, 2, 4, 5)  # Adding multiple elements

print("LinkedList:", ll)
print("Search 3 position:", ll.search(3))
ll.insert(2, 3)
print("After Inserting 3:", ll)
ll.remove(3)
print("After Removing 3:", ll)
ll.reverse()
print("Reversed LinkedList:", ll)

# Iterating through LinkedList
print("Iterating through LinkedList:")
for item in ll:
    print(item)
