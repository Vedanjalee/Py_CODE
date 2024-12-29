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
        if pos < 0:
            return
        loop_node, current = None, self.head
        index = 0
        while current.next:
            if index == pos:
                loop_node = current
            current = current.next
            index += 1
        current.next = loop_node

    def detect_and_remove_loop(self):
        slow, fast = self.head, self.head

        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  
                print("Loop detected.")
                self.remove_loop(slow)
                return
        print("No loop found.")

    def remove_loop(self, loop_node):
        ptr1 = self.head
        ptr2 = loop_node

        
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        
        print(f"Start of loop detected at node with data: {ptr1.data}")
        ptr2 = loop_node
        while ptr2.next != ptr1:  
            ptr2 = ptr2.next
        ptr2.next = None
        print("Loop removed.")

    def display(self):
        
        current = self.head
        visited = set()
        while current:
            if current in visited:  
                print(f"({current.data}) -> LOOP")
                break
            print(current.data, end=" -> ")
            visited.add(current)
            current = current.next
        else:
            print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)


print("Original List:")
ll.display()


ll.create_loop(2)  
print("\nList with Loop:")
ll.display()

ll.detect_and_remove_loop()

print("\nList after Removing Loop:")
ll.display()
