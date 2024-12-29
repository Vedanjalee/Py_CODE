class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at_position(self, data, position):
        if position < 1:
            print("Position should be >= 1")
            return

        new_node = Node(data)
        if position == 1:
            self.insert_at_beginning(data)
            return

        current = self.head
        for i in range(position - 2): 
            if current is None:
                print("Position out of range")
                return
            current = current.next

        if current is None:  
            print("Position out of range")
            return

        new_node.next = current.next
        new_node.prev = current
        if current.next:  
            current.next.prev = new_node
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


dll = DoublyLinkedList()

dll.insert_at_beginning(10)
dll.insert_at_beginning(20)

dll.insert_at_end(30)
dll.insert_at_end(40)


dll.insert_at_position(25, 3)  
dll.insert_at_position(5, 1)   

dll.insert_at_position(50, 10)  

dll.display()

