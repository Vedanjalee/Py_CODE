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

    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True  

        
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reverse_list(slow)

        first_half = self.head
        palindrome = True
        temp = second_half  

        while temp:
            if first_half.data != temp.data:
                palindrome = False
                break
            first_half = first_half.next
            temp = temp.next

       
        self.reverse_list(second_half)

        return palindrome

    def reverse_list(self, head):
        prev, current = None, head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(1)

if ll.is_palindrome():
    print("palindrome.")
else:
    print("not palindrome.")
