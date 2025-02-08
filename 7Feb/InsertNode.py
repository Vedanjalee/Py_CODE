class Node:
    def __init__(self, data1, next1= None):
        self.data = data1 
        self.next = next1 

y = Node(2) 
y2 = Node(3)
print(y.data, end =" -> ")
print(y2.data)