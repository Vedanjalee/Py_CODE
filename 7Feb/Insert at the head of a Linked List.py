class Node :
    def __init__(self, data1, next1 = None ):
        self.data = data1 
        self.next = next1 

def printLL(head) :
    while head is not None : 
        print(head.data, end ="->")

        head = head.next 
    print(None)


def insertHead(head, val) :
    temp = Node(val, head) 
    return temp 

arr = [12, 8, 5, 7] 
val = 100 

head = Node(arr[0])
head.next = Node(arr[1]) 
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])

head = insertHead(head, val) 

printLL(head)