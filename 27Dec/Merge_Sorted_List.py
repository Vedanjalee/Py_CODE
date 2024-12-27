class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

def merge_sorted_list(l1, l2 ):
    dummy = Node(0)
    tail = dummy 


    while l1 and l2 :
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next 
        else:
            tail.next = l2
            l2 = l2.next 
        tail = tail.next 


    if l1: 
        tail.next = l1 
    if l2 : 
        tail.next = l2 

    return dummy.next 

def create_linked_list (values):
    if not values: 
        return None 
    head = Node(values[0])
    current = head 
    for value in values[1:]:
        current.next = Node(value)
        current = current.next 
    return head 

def Display(head):
    result = []
    current = head 
    while current:
        result.append(current.data)    
        current = current.next 
    print(" -> ".join(map(str, result))) 


list1 = [1, 3, 5]
list2 = [2, 4, 6]     
                           
l1 = create_linked_list(list1)
l2 = create_linked_list(list2)

print("List 1:")
Display(l1)
print("List 2:")
Display(l2)

merged_list = merge_sorted_list(l1, l2)
print("Merged List:")
Display(merged_list)