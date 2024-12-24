class Node :
    def __init__(self,data):
        self.data = data 
        self.next = None

class Singly_LL:
    def __init__(self):
        self.head = None 

    def insert_at_kth(self,data,k):
        new_node = Node(data)
        if k== 1:

            new_node.next = self.head 
            self.head = new_node 
       
            print(data, "inserted at the position " , k )
            return 
        current = self.head 
        count = 1

        while current is not None and count < k - 1:
            current = current.next
            count += 1
        
        if current is None:  # If position is invalid
            print(k," is out of range")
            return
        
        new_node.next = current.next
        current.next = new_node
        print(data,"inserted at position ", k)

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

linked_list.insert_at_kth(10, 1) 
linked_list.insert_at_kth(20, 2) 
linked_list.insert_at_kth(15, 2)  
linked_list.insert_at_kth(30, 5) 

print("After inserting at head:")
linked_list.display()