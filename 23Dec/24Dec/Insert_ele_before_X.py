class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
class LinkedList:
    def __init__(self) :
        self.head =None 

    def insert_before_x (self, data, x):
        new_node = Node(data) 

        if not self.head :
            print("the lit is empty")
            return 
        if self.head.data == x:
            new_node.next  = self.head 
            self.head = new_node 
            return 

        current = self.head 
        while current.next and current.next.data != x:
            current = current.next 

        if not current.next: 
            print(x," not foun din the list" )
            return 

        new_node.next = current.next 
        current.next = new_node 

    def display(self):
        current = self.head 
        while current: 
            print(current.data, end =" -> ")
            current = current.next 
        print("None")

ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)

ll.display()  

ll.insert_before_x(15, 20)
ll.display()

ll.insert_before_x(5,10)
ll.display()

ll.insert_before_x(25, 100)