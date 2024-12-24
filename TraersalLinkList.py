class Node : 
    def __init__ (self,data):
        self.data = data
        self.next = None 

class Singly_Link_List():
    def __init__(self):
        self.head = None 

    def traversal(self):
        if self.head is None: 
            print("Singly LinkedList is Empty")
        else:
            start = self.head 
            while start is not None:
                print(start.head, end =" ") 
                start = start.next 
                       
