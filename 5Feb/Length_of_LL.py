
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def detect_loop(head):
    
    slow = head  
    
    
    fast = head 

    
    while fast is not None and fast.next is not None:
       
        slow = slow.next  
        fast = fast.next.next  

        if slow == fast:
            return True

   
    return False



def find_loop_length(head):
    slow = head
    fast = head

   
    while fast is not None and fast.next is not None:
        
        slow = slow.next     
        
        fast = fast.next.next  

        
        if slow == fast:
           
            length = 1  
             
            fast = fast.next 

            
            while slow != fast:
                
                fast = fast.next  
                
                length += 1  

            
            return length

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  


if detect_loop(head):
    
    length = find_loop_length(head)
    print(f"The length of the loop is: {length}")
else:
    print("No loop found in the linked list.")

