class Node :
    def __init__(self,data):
        self.data = data 
        self.next = None

class Singly_LL:
    def __init__(self):
        self.head = None 

    def insert_head(self,data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node 
       
        print(data, "inserted at the head")

    def display(self):
        if self.head is None:
            print("Linked List is EMPTY")
        else:
            current = self.head 
            while current is not None :
                print(current.data, end = " -> ")  
                current = current.next 
            print("None")

linked_list = Singly_LL()      
linked_list.insert_head(10)
linked_list.insert_head(20)
linked_list.insert_head(30)

print("After inserting at head:")
linked_list.display()