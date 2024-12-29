class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 
def delete_node(head, value):
    if not head:
        return head 

    if head.value == value:
        return head.next 
    current= head 

    while current.next and current.next.value != value :
        current = current.next 
    if current.next :
        current.next = current.next.next 
    return head    

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


head = delete_node(head, 20)
print_list(head)
