class Node :
    def __init__(self,value):
        self.value = value
        self.prev = None 
        self.next = None 

def print_list(head):
    current = head 
    result =[]
    while current:
        result.append(current.value)
        current = current.next 
    print("doubly LL", result)     

def insert_at_beginning(head, value):
    new_node = Node(value)
    if head is not None :
        new_node.next = head 
        head.prev = new_node 
    return new_node  

head = Node(10)
node2 = Node(20)
node3 = Node(30)
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2

# Print the list before inserting a new head
print("Before insertion:")
print_list(head)

# Insert at the beginning
head = insert_at_beginning(head, 5)

# Print the list after inserting a new head
print("After insertion:")
print_list(head)