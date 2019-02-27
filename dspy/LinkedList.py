class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next is not None:
            last = last.next

        last.next = new_node

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def remove(self, data):
        node = self.head

        if node.data is data:
            self.head = None
            return self.head

        while node.next is not None:
            if node.next.data is data:
                node.next = node.next.next
                return self.head
            node = node.next

        return self.head

    def print_all(self):
        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print("")

