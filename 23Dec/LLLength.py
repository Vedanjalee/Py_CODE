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
        temp = self.head
        while temp.next:  
            temp = temp.next
        temp.next = new_node    

    def length(ll):
        count = 0
        temp = ll.head
        while temp:
           count += 1
           temp = temp.next
        return count


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print(ll.length())  
