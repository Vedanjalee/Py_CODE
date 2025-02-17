class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def LLIdentical(head1, head2):
    while head1 and head2:
        if head1.data != head2.data:
            return False
        head1, head2 = head1.next, head2.next
    
    return head1 is None and head2 is None  


head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)

head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)

if LLIdentical(head1, head2):
    print("Linked lists are identical.")
else:
    print("Linked lists are not identical.")
