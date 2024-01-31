class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.link:
                current = current.link
            current.link = Node(data)

    def search(self, target):
        pre = None
        cur = self.head

        while cur and target > cur.data:
            pre = cur
            cur = cur.link

        flag = False
        if cur and cur.data == target:
            flag = True

        # Returning the data of pre and cur nodes, and the flag status
        pre_data = pre.data if pre else None
        cur_data = cur.data if cur else None
        return pre_data, cur_data, flag

# Example usage
ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(4)
ll.add(5)

pre_data, cur_data, flag = ll.search(3)
print("Pre:", pre_data, "Cur:", cur_data, "Found:", flag)
