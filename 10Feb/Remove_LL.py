class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def removeElements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head
    current = dummy

    while current and current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    return dummy.next

def printLinkedList(head: ListNode):
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result) if result else "Empty list")


values = [1, 2, 6, 3, 4, 5, 6]
target_value = 6

print("Original Linked List:")
head = createLinkedList(values)
printLinkedList(head)

print(f"Removing elements with value {target_value}:")
new_head = removeElements(head, target_value)
printLinkedList(new_head)
