# class Node:
#     def __init__(self, data):
#         self.data = data  
#         self.next = None 


# class SLL:
#     def __init__(self):
#         self.head = None 

#     def insert_Begin(self, new_data):
#         new_node = Node(new_data)
#         new_node.next =  self.head
#         self.head = new_node 

#     def printList(self):
#         temp = self.head  
#         while temp:      
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")     
    

# ll = SLL()
# ll.insert_Begin(10)
# ll.insert_Begin(20)  
# ll.printList()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = next 

class SLL:
    def __init__(self):
        self.head = None 

    def insert_begin(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head = new_node

    def display(self):
        temp = self.head 
        while temp :
            print(temp.data , end =" -> ")
            temp = temp.next 
        print("None")

LL = SLL()
LL.insert_begin(10)
LL.insert_begin(20)
LL.display()