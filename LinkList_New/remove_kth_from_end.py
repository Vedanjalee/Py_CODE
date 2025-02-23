class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_kth_from_end(head, k):
    dummy = ListNode(0, head)
    fast = slow = dummy
    
    for _ in range(k + 1):
        if fast:
            fast = fast.next
    
    while fast:
        fast = fast.next
        slow = slow.next
    
    
    if slow.next:
        slow.next = slow.next.next
    
    return dummy.next


def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
head = remove_kth_from_end(head, k)
print_list(head) 
