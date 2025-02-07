class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next or not head.next.next:
            return

    
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        slow.next = None 
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node


        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()


values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

print("Original Linked List:")
print_linked_list(head)

solution = Solution()
solution.reorderList(head)

print("Reordered Linked List:")
print_linked_list(head)
