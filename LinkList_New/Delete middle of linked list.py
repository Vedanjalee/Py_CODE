class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteMid(head) :

    if head is None :
        return None 
    
    if head.next is None :
        return None 
    
    prev  = None 
    slow = head 
    fast = head 

    while fast is not None and fast.next is not None :
        fast = fast.next.next 

        prev = slow 
        slow = slow.next 

    prev.next = slow.next 

    return head 


def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")    

head = Node(1) 
head.next = Node(2)  
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original Linked List: ", end="")
printList(head)

head = deleteMid(head)

print("Linked List after deleting the middle node: ", end="")
printList(head)

    