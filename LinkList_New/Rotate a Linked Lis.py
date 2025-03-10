class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insertNode(head, val):
    newNode = Node(val) 
    if head == None:
        head = newNode 
        return head 
    temp = head 
    while temp.next != None :
        temp = temp.next 
    temp.next = newNode 
    return head 

def rotateRight(head, k):
    if head == None or head.next == None:    
        return head 
    for i in range(k):
        temp = head 
        while temp.next.next !=None :
            temp = temp.next 
        end = temp.next 
        temp.next = None 
        end.next = head 
        head = end 
    return head        

def printList(head):
    while head.next != None:
        print(head.val, end='->')
        head = head.next
    print(head.val)
    return

if __name__ == '__main__':
    head = None
    
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 5)


    print("Original list: ", end='')
    printList(head)


    k = 2
    newHead = rotateRight(head, k)


    print("After", k, "iterations: ", end='')
    printList(newHead) 