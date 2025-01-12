class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class SLL:
    def __init__(self):
        self.head = None 

    def Traversal(self):
        if self.head is None:
            print("SLL is empty")
            return 
        
        start = self.head 
        while start is not None :
            print(start.data, end =" ")
            start = start.next 
            

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
                       
linked_list = SLL()

linked_list.head = node1  
node1.next = node2  
node2.next = node3  

linked_list.Traversal()