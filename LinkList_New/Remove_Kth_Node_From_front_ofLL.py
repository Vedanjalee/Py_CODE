class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_kth_from_front(head,k) :
    if not head:
        return None
    
    
    if k == 1:
        return head.next
    
    current = head
    prev = None
    
    for _ in range(k - 1):
        if not current:
            return head  
        prev = current
        current = current.next
    
    if prev and current:
        prev.next = current.next
    
    return head

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 3
head = remove_kth_from_front(head, k)
print_list(head)  
