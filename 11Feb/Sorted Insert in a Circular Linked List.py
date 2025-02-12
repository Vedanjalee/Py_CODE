class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def sortedInsert(self, data):
        new_node = Node(data)

        # If empty

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return

        current = self.head

        #  Insert before the head (smallest element)
       
        if data <= self.head.data:
           
            while current.next != self.head:
                current = current.next

           
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
            return

        
        while current.next != self.head and current.next.data < data:
            current = current.next

        
        new_node.next = current.next
        current.next = new_node

    def display(self):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        nodes = []
        while True:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        print(" -> ".join(nodes))


cll = CircularLinkedList()
cll.sortedInsert(30)
cll.sortedInsert(10)
cll.sortedInsert(20)
cll.sortedInsert(25)
cll.sortedInsert(5)

print("Circular Linked List after sorted insertions:")
cll.display()
