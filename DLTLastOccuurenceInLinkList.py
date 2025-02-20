
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteLastOccurrence(head, key):
    prev = None
    last = None
    prev_last = None
    current = head

    # Traverse the list to find the last occurrence
    while current:
        if current.val == key:
            last = current
            prev_last = prev  # Track the node before last occurrence
        prev = current
        current = current.next

    # If the key was never found, return the original list
    if last is None:
        return head

    # If last occurrence is the head node
    if last == head:
        return head.next

    # Delete the last occurrence
    prev_last.next = last.next
    return head

# Helper function to create a linked list from a list
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example Usage:
head = createLinkedList([1, 2, 3, 5, 2, 10])
print("Original List:")
printLinkedList(head)

key = 2
head = deleteLastOccurrence(head, key)

print("After Deleting Last Occurrence of", key, ":")
printLinkedList(head)
