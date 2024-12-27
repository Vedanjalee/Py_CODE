class Node :
    def __init__(self,data):
        self.data = data 
        self.next = None 

class SLL:
    def __init__(self):
        self.head = None 

    def insert_begin(self,new_data) :
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head = new_node 

    def deleteNode(self, key):
        temp =   self.head 

        if temp and temp.data == key :
            self.head = temp.next 
            return 

        prev = None 
        while temp and temp.data != key:
            prev = temp 
            temp = temp.next 

        if not temp:
            print("Key not found ")
            return   
        prev.next = temp.next   

    def print_list(self):
        temp = self.head 
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next 
        print("None")

LL = SLL()
LL.insert_begin(40)
LL.insert_begin(30)
LL.insert_begin(20)
LL.insert_begin(10)
LL.deleteNode(20)
LL.print_list()
