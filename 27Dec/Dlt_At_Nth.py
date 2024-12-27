class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class SLL:
    def __init__(self) :
        self.head = None 

    def insert_begin(self,new_data):
        new_node =Node(new_data)           
        new_node.next = self.head 
        self.head = new_node 

    def delete_at_position(self,posi)    :
        if posi<1:
            print("posi should be greater thn one")
            return 

        if posi == 1:
            self.head = self.head.next 
            return 
        
        temp = self.head 
        for i in range(posi-2):
            if not temp or not temp.next:
                print("posi out of range")
                return 
            temp = temp.next 

        if not temp.next:
            print("out of range")
            return 

        temp.next = temp.next.next 

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


LL = SLL()


LL.insert_begin(10)
LL.insert_begin(20)
LL.insert_begin(30)
LL.insert_begin(40) 


print("Before List:")
LL.display()


LL.delete_at_position(3)  

print("new Updated List:")
LL.display()

