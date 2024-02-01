class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.link:
                current = current.link
            current.link = Node(data)
        self.size += 1

    def remove(self, data):
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.link

        if current:
            if previous:
                previous.link = current.link
            else:
                self.head = current.link
            self.size -= 1
            return True
        else:
            return False

    def insert(self, index, data):
        if index > self.size:
            return False  # Index out of bounds
        new_node = Node(data)
        if index == 0:
            new_node.link = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.link
            new_node.link = current.link
            current.link = new_node
        self.size += 1
        return True

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.link
            current.link = prev
            prev = current
            current = next_node
        self.head = prev

    def search(self, target):
        current = self.head
        while current and current.data != target:
            current = current.link
        return current is not None

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.link
        return ' -> '.join(elements)

# Example usage
ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(4)
ll.add(5)

print("LinkedList:", ll)
print("Search 3:", ll.search(3))
ll.insert(2, 3)
print("After Inserting 3:", ll)
ll.remove(3)
print("After Removing 3:", ll)
ll.reverse()
print("Reversed LinkedList:", ll)
