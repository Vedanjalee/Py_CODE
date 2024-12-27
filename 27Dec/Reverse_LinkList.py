class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def reverse_list(head):
    prev = None 
    curr = head 

    while curr:
        next_node = curr.next 
        curr.next = prev 
        prev = curr 
        curr = next_node 
    return prev 

def create_LL(values):
    if not values :
        return None 

    head = Node(values[0])
    current = head 
    for value in values[1:]:
        current.next = Node(value) 
        current = current.next 
    return head 

def display_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    print(" -> ".join(map(str, result)))     

values = [1,2,3,4,5]
head = create_LL(values)      

print("Original list: ")
display_linked_list(head)

head = reverse_list(head)
print("Reversed List:")
display_linked_list(head)