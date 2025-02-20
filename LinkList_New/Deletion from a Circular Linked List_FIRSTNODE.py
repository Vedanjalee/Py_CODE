class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteFirstNode(last) :
    if last is None :
        print("list is empty")
        return None

    head = last.next 

    if head == last :
        last = None 

    else:
        last.next = head.next 

    return last 

def print_list(last) :
    if last is None :
        return

    head = last.next 
    while True:
        print(head.data, end = " ")
        head = head.next 
        if head == last.next :
            break 
    print() 

first = Node(2)
first.next = Node(3)
first.next.next = Node(4)

last = first.next.next
last.next = first

print("Original list: ", end="")
print_list(last)



last = deleteFirstNode(last)

print("List after deleting first node: ", end="")
print_list(last)
