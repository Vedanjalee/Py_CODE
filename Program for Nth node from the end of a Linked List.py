class Node: 
    def __init__(self, val = 0, next=None) :
        self.val = val 
        self.next = next 

def findNthFromEnd(head , N) :
    fast = slow = head 

    for _ in range(N) :
        if fast is None : 
            return None 
        fast = fast.next    
   
    while fast : 
        fast = fast.next 
        slow = slow.next 
    return slow.val 

def createLinkedList(arr):
    if not arr :
        return None 

    head = Node(arr[0]) 
    curr = head 
    for val in arr[1:] :
        curr.next = Node(val) 
        curr = curr.next 
    return head       

head = createLinkedList([1, 2, 3, 4, 5])
N = 2
print(findNthFromEnd(head, N))

