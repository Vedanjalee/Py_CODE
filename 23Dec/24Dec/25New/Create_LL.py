class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 

def print_list(head):
    current = head 
    while current:
        print(current.value, end=" -> ")
        current = current.next 
    print("None")

head = Node(10)
node2 = Node(20)
node3 = Node(30)
head.next = node2
node2.next = node3


print_list(head)
