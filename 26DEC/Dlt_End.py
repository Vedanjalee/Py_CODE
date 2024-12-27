class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class SLL:
    def __init__(self):
        self.head = None 

    def insert(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head = new_node 

    def dlt_end(self):  
        if not self.head :
            print("The list is Empty.Nothing to dlt")
            return 
        
        if not self.head.next:
            self.head = None 
            return 
        
        temp = self.head 
        while temp.next and temp.next.next :
            temp = temp.next 
        temp.next = None

    def display(self):
        temp = self.head 
        while temp :
            print(temp.data, end=" -> ")
            temp = temp.next 
        print("None ")

LL = SLL()
LL.insert(10)
LL.insert(20)
LL.insert(30)

print("List before deletion:")
LL.display()

LL.dlt_end()
print("List after deleting the last node:")
LL.display()