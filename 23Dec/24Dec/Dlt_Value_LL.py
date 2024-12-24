class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class Singly_LL:
    def __init__(self):
        self.head = None 

    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
        else:
            current = self.head 
            while current.next is not None:
                current = current.next 
            current.next = new_node 

    def delete_value (self,value):
            if self.head is None:
                print("empty, nothing to dlt")
                return 
            if self.head.data == value :
                self.head = self.head.next 
                print(value,"dlt")
                return 
            current = self.head
            while current.next is not None and current.next.data != value:
                current = current.next  # Traverse the list

            if current.next is None:  # If we reach the end of the list
                print(f"Value {value} not found in the list.")
                return

            current.next = current.next.next 
            print(value,"dlted")    

    def display (self):
            if self.head is None:
                print("ll is emoty") 
            else: 
                current = self.head 
                while current is not None:
                    print(current.data, end =" -> ")
                    current = current.next 
                print("None")

linked_list = Singly_LL()


linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(40)
linked_list.insert(50)


print("Before deletion:")
linked_list.display()

linked_list.delete_value(30)  
linked_list.display()

linked_list.delete_value(10) 
linked_list.display()

linked_list.delete_value(100)