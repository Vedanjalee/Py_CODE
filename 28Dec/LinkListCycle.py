class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None  

    def Insert_end(self, data):
        new_node = Node(data)
        if not self.head:  
            self.head = new_node
            return
        current = self.head
        while current.next:  
            current = current.next
        current.next = new_node

    def create_cycle(self, position):
        
        if position < 0:
            return
        cycle_node = None
        current = self.head
        count = 0
        while current:
            if count == position:  
                cycle_node = current
            if not current.next:  
                current.next = cycle_node  
                return
            current = current.next
            count += 1

    def detect_cycle(self):
        
        slow = self.head  
        fast = self.head  

        while fast and fast.next:  
            slow = slow.next  
            fast = fast.next.next  
            if slow == fast:  
                return True

        return False  
    
ll = LinkedList()
ll.Insert_end(1)
ll.Insert_end(2)
ll.Insert_end(3)
ll.Insert_end(4)
ll.Insert_end(5)

print("Cycle check before creating a cycle:")
print("Cycle in LL?" , ll.detect_cycle())  


ll.create_cycle(1)

print("Cycle detection after creating a cycle:")
print("Cycle in LL?" , ll.detect_cycle())  

