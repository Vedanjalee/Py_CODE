class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

new_node = Node(10)
print(new_node.data, end=" -> ")
print(new_node.next)        

