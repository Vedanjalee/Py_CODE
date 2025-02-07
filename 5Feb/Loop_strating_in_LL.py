class Node:
    def __init__(self, data, next_node=None):
        
        self.data = data  
       
        self.next = next_node  


def first_node(head):
   
    slow = head
    fast = head

    
    while fast is not None and fast.next is not None:
        
        slow = slow.next

        
        fast = fast.next.next

        
        if slow == fast:
            
            slow = head

           
            while slow != fast:
                
                slow = slow.next
                fast = fast.next

                
            return slow

    
    return None
    

node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5


node5.next = node2


head = node1

loop_start_node = first_node(head)

if loop_start_node:
    print("Loop detected. Starting node of the loop is:", loop_start_node.data)
else:
    print("No loop detected in the linked list.")
                                
                            