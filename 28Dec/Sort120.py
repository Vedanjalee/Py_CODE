class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def sort_0s_1s_2s(self):
        count = {0: 0, 1: 0, 2: 0}
        current = self.head
        while current:
            count[current.data] += 1
            current = current.next

        current = self.head
        for value in range(3):  
            while count[value] > 0:
                current.data = value
                current = current.next
                count[value] -= 1

    def display(self):
        """Display the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create the linked list
ll = LinkedList()
ll.append(0)
ll.append(1)
ll.append(2)
ll.append(1)
ll.append(0)
ll.append(2)
ll.append(1)

print("Original List:")
ll.display()

ll.sort_0s_1s_2s()

print("Sorted List:")
ll.display()
