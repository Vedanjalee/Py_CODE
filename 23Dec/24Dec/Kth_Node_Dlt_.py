class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Singly_LL:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head = new_node 
        else:
            current = self.head 
            while current.next is not None:
                current = current.next 
            current.next = new_node 

    def delete_kth_node(self, k) :
        if self.head is None:   
            print("list i semppty, nothing to dlt")
            return 

        if k==0 :
            self.head = self.head.next
            return 

        current = self.head 
        count = 0


        while current is not None and count < k-1:
            current = current.next 
            count += 1

        if current is None or current.next is None:
            print(k, "is out of range")
            return 

        current.next = current.next.next

    def display  (self):
        if self.head is None:
            print("list is empty")
        else:
            current = self.head
            while current is not None: 
                print(current.data, end=" -> ") 
                current = current.next  
            print("None")

linked_list = Singly_LL()

linked_list.insert(10);
linked_list.insert(20);
linked_list.insert(30);
linked_list.insert(40);
linked_list.insert(50);

print("Before deletion:")
linked_list.display()

linked_list.delete_kth_node(2)

print("After deleting 2nd node:")
linked_list.display()

linked_list.delete_kth_node(10) 

