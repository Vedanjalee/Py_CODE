class Node : 
    def __init__ (self,data):
        self.data = data
        self.next = None 

class Singly_Link_List():
    def __init__(self):
        self.head = None 

    def traversal(self):
        if self.head is None: 
            print("Singly LinkedList is Empty")
        else:
            start = self.head 
            while start is not None:
                print(start.data, end =" ") 
                start = start.next 

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
                       
linked_list = Singly_Link_List()

linked_list.head = node1  
node1.next = node2  
node2.next = node3  

linked_list.traversal()