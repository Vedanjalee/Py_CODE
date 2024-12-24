class Node :
    def __init__(self,data):
        self.data = data 
        self.next = None 

class Singly_Linked_List:
    def __init__(self):
        self.head= None 

    def insert(self, data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node 
        else:
            current = self.head 
            while current.next is not None:
                current = current.next 
            current.next = new_node 
 
    def delete_tail(self):
        if self.head is None :
            print("list already empty")
            return 
        
        if self.head.next is None:
            self.head = None 
            return 
        
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next 
  
        temp.next = None                     
    
    def display(self):
        if self.head is None:  
            print("List is empty!")
        else:
            current = self.head  
            while current is not None:  
                print(current.data, end=" → ") 
                current = current.next
            print("None")  
linked_list = Singly_Linked_List()

linked_list.insert(10)  
linked_list.insert(20)  
linked_list.insert(30)  
linked_list.insert(40)  

print("Before deleting head:")
linked_list.display()

linked_list.delete_tail()

print("After deleting head:")
linked_list.display()