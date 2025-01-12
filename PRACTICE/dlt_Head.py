class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class SLL:
    def __init__(self):
        self.head = None 

    def insert(self,data ):
        new_node =Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head 
            while current.next is not None:
                current = current.next 
            current.next = new_node 


    def dlt(self):
        if self.head is None:
            print("empty ")
        else:
            self.head = self.head.next       

    def display(self):
        if self.head is None:
            print("already sorted")
        else:    
            current = self.head 
            while current is not None:
                print(current.data, end =" -> ")
                current = current.next
            print("None")    

LL= SLL()

LL.insert(10)  
LL.insert(20) 
LL.insert(30)  
LL.insert(40) 

print("Before deleting head:")
LL.display()


LL.dlt()

print("After deleting head:")
LL.display()                 
    