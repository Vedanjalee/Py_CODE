class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def reverse(head):
    prev, curr = None, head
    while curr:
        next_node = curr.next  
        curr.next = prev  
        prev = curr  
        curr = next_node  
    return prev  


def areListsIdentical(head1, head2):
    while head1 and head2:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next
    return head1 is None and head2 is None  


def areMirrors(head1, head2):
    return areListsIdentical(head1, reverse(head2))


def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    temp = head
    for val in arr[1:]:
        temp.next = Node(val)
        temp = temp.next
    return head


def printLinkedList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]

head1 = createLinkedList(arr1)
head2 = createLinkedList(arr2)

print("Linked List 1:")
printLinkedList(head1)

print("Linked List 2:")
printLinkedList(head2)

if areMirrors(head1, head2):
    print("The linked lists are mirror images of each other.")
else:
    print("The linked lists are NOT mirror images.")
