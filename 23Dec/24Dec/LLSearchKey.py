class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class Singly_Linked_List:
    def __init__(self):
        self.head = None  

    def insert(self, data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:  
                current = current.next
            current.next = new_node  
    def search_key(self, key):
        current = self.head  
        position = 0  
        while current is not None:
            if current.data == key:  
                return (key, position,"this is value and its position")
            current = current.next  
            position += 1  
        return ("key not found")
   

linked_list = Singly_Linked_List()

linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(40)

print(linked_list.search_key(20))  
print(linked_list.search_key(50))  
