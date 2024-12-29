class DLNode:
    def __init__(self,val=0,next=None,prev=0):
        self.val = val 
        self.prev = prev 
        self.next = next 

def Arr_to_DLL(arr):
    if not arr: 
        return None 
    
    head = DLNode(arr[0])
    current = head 

    for value in arr[1:]:
        new_node = DLNode(value)
        current.next = new_node 
        new_node.prev = current 
        current = new_node 

    return head 

def print_forward(head):
    result =[]
    while head: 
        result.append(head.val)
        head = head.next 
    print("doubly liked list ", result )

arr = [10,20,30,40,50]
head =   Arr_to_DLL(arr)
print_forward(head)        
