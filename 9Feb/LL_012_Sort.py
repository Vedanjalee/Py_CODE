
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    # Append elements to the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def sortList(self,head):
        count = [0,0,0]
        temp = self.head

        while temp is not None:
            count[temp.data] += 1
            temp = temp.next 

        i = 0 
        temp = self.head 


        while temp is not None : 
            if count[i] == 0 :
                i += 1
            else :
                temp.data = i
                count[i] -= 1 
                temp = temp.next         

    # Print the elements of the linked list
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Test the code
sll = SLL()
sll.append(2)
sll.append(1)
sll.append(0)

print("Original Linked List:")
sll.printLinkedList()

sll.sortList()

print("Sorted Linked List:")
sll.printLinkedList()
