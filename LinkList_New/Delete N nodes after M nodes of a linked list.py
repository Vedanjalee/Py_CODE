class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_N_after_M(head, M, N):
    curr = head

    while curr:

        for i in range(M-1):
            if curr is None:
                return head
            curr = curr.next 

        if curr is None or curr.next is None :
            return head 

        temp = curr.next
        for i in range(N):
            if temp is None :
                break 

            temp = temp.next 

        curr.next = temp 
        curr = temp

    return head 

def print_list(head) :
    curr = head 
    while curr:
        print(curr.val , end = " -> ") 
        curr = curr.next 
    print("None")

head = Node(1, Node(2, Node (3, Node (4, Node( 5, Node( 6, Node( 7, Node(8, Node(9, Node(10))))))))))

print("original list")

print_list(head)

M,N = 2,2

head = delete_N_after_M(head, M, N)

print("Modified List: ")
print_list(head)