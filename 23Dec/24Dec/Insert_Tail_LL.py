class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Singly_LL:
    def __init__(self):
        self.head = None 

    def insert_tail(self,data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node 
            print(data,"insereted at the tail")
            return 
        current = self.head 
        while current.next is not None :
            current = current.next 
        current.next = new_node 
        print(data, " inserted at the tail")
    def display(self):
        if self.head is None:
            print("LL is empty ")
        else:
            current = self.head 
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next 
            print("None")      
linked_list = Singly_LL()

linked_list.insert_tail(10)
linked_list.insert_tail(20)
# linked_list.insert_tail(30) 

print("After inserting at tail:")
linked_list.display()