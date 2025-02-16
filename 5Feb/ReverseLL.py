class Node : 
    def __init__(self, data) :
        self.data = data 
        self.next = None

class LinkedList: 
    def __init__(self) :
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


    def reverse(self):
        prev = None
        current = self.head

        while current : 
            next_node = current.next 
            current.next = prev 
            prev = current 
            current = next_node 
        self.head = prev 


    def display(self) :
        current = self.head 
        while current : 
            print(current.data, end = " -> ")
            current = current.next 
        print("None")       

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Original Linked List:")
ll.display()


# Reverse the linked list
ll.reverse()
print("Reversed Linked List:")
ll.display()
   
