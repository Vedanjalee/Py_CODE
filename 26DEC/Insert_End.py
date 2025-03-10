
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class SLL:
    def __init__(self):
        self.head = None 

    def insert_end(self,new_data):
        new_node = Node(new_data)    
        if not self.head :
            self.head=new_node
            return 
        temp = self.head 
        while temp.next:
            temp = temp.next 
        temp.next = new_node 


    def display(self):
        temp = self.head 
        while temp :
            print(temp.data, end =" -> ")
            temp = temp.next 
        print("None")     

LL = SLL()

LL.insert_end(40)
LL.insert_end(30)
LL.display()
        

