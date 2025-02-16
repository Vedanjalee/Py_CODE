class Node : 

    def __init__(self, data) :

        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self) :
        self.head = None 

    def append(self,data):
        new_node = Node(data) 
        if not self.head :
            self.head = new_node 
            return 

        current = self.head 
        while current.next :
            current = current.next 
        current.next = new_node 

    def middle_ele_finding(self) :
        slow = self.head 
        fast = self.head

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

        return slow.data if slow else None 

    def display(self):
        current = self.head 
        while current:
            print(current.data, end =  " -> ")
            current = current.next 
        print("None......") 



ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Original Linked List:")
ll.display()

middle_value = ll.middle_ele_finding()
print(f"Middle Node: {middle_value}")





