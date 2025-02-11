class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicates(head) :
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def printLinkedList(head):
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result) if result else "Empty list")


values = [1, 1, 2, 3, 3]

head = createLinkedList(values)
print("Original Linked List:")
printLinkedList(head)


print("After Removing Duplicates:")

new_head = removeDuplicates(head)
printLinkedList(new_head)
