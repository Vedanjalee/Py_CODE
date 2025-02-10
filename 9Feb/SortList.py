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

    # Sort linked list containing 0s, 1s, and 2s
    def sortList(self):
        # Count occurrences of 0s, 1s, and 2s
        count = [0, 0, 0]
        temp = self.head

        # Count the occurrences
        while temp:
            count[temp.data] += 1
            temp = temp.next

        # Overwrite the linked list data based on counts
        i = 0
        temp = self.head

        while temp:
            if count[i] == 0:
                i += 1
            else:
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
sll.append(1)
sll.append(0)
sll.append(2)
sll.append(1)
sll.append(0)

print("Original Linked List:")
sll.printLinkedList()

sll.sortList()

print("Sorted Linked List:")
sll.printLinkedList()
