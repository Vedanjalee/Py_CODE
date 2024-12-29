class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def create_loop(self, pos):
        if pos == -1:
            return
        loop_start = self.head
        tail = self.head
        count = 0

        while tail.next:
            tail = tail.next
            if count < pos:
                loop_start = loop_start.next
                count += 1

        tail.next = loop_start

    def find_loop_start(self):
        slow = self.head
        fast = self.head

        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow.data

        return None 


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.create_loop(2) 

loop_start = ll.find_loop_start()
if loop_start:
    print("Loop starts at node with value:", loop_start)  
else:
    print("No loop detected.")
