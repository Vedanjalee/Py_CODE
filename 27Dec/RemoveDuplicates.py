class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

def remove_duplicates(head):
    curr = head 
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next 
        else:
            curr= curr.next 
    return head 

def create_linked_list(values):
    if not values:
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

values = [1, 1, 2, 3, 3, 4, 5, 5]
head = create_linked_list(values)

print("Original List:")
display_linked_list(head)


head = remove_duplicates(head)

print("List After Removing Duplicates:")
display_linked_list(head)