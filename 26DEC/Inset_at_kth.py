# class Node:
#     def __init__(self,data):
#         self.data = data 
#         self.next = None 

# class SLL:
#     def __init__(self):
#         self.head = None 

#     def insertAtBeginning(self,new_data):
#         new_node = Node(new_data)
        
#         if not self.head:
#             self.head = new_node 
#             return 
#         temp = self.head 
#         while temp.next:
#             temp =temp.next 
#         temp.next = new_node 

#     def insertAtPosition(self, position, new_data):
#         if position < 1:
#             print("position must be 1 or greater")
#             return 
#         new_node = Node(new_data)

#         if position == 1:
#             new_node.next = self.head
#             self.head = new_node 
#             return 
        
#         temp = self.head 
#         for  i  in range(position - 2):
#             if not temp:
#                 print("Position out of range")
#                 return 
#             temp = temp.next
#         new_node.next = temp.next 
#         temp.next = new_node   


#     def printList(self):
#         temp = self.head  
#         while temp:       
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")         

# ll = SLL()
# ll.insertAtBeginning(10)
# ll.insertAtBeginning(20)
# ll.insertAtBeginning(30)
# ll.insertAtBeginning(40)
# ll.insertAtPosition(3, 15)

  
# print("Linked List:")
# ll.printList()  

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class SLL:
    def __init__(self):
        self.head = None

    def insert_begin(self, new_data) :
        new_node = Node(new_data)           
        new_node.next = self.head
        self.head = new_node 

    def K_posi(self, posi, new_data):
        if posi< 1:
            print("Ned greater ") 
            return

        new_node = Node(new_data)
        if posi ==  1:
            new_node.next = self.head
            self.head = new_node 
            return 
      
        temp = self.head 
        for i in range(posi - 2):
            if not temp:
                print("posi_out o frange")
                return 
            temp = temp.next 

        new_node.next = temp.next    
        temp.next = new_node 

    def display (self):
        temp = self.head
        while temp:
            print(temp.data, end= "->") 
            temp = temp.next 
        print("none")    

LL=SLL()
LL.insert_begin(20)
LL.insert_begin(20)
LL.insert_begin(40) 

LL.K_posi(2,13)
LL.display()






