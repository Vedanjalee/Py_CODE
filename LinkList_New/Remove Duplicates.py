class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    curr = head 

    while curr and curr.next :
        if curr.val == curr.next.val:
            curr.next = curr.next.next 
        else:
            curr = curr.next 
    return head    


def print_list(head):
    curr = head 
    while curr :
        print(curr.val, end =" -> ")
        curr = curr.next 
    print("None")    


head=Node(3, Node(5, Node(5, Node(6, Node(7)))))  


print_list(head)  

head = remove_duplicates(head)

print("after removing duplicates")
print_list(head) 