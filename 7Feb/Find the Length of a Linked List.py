class Node :
    def __init__(self, data, next_node = None ):
        self.data = data 
        self.next = next_node 


def lenght_of_LL(head):
    cnt = 0 
    temp = head 

    while temp is not None :
        temp = temp.next 
        cnt += 1

    return cnt 

arr = [2, 5, 8, 7]
   
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])

print("Length of the linked list:", lenght_of_LL(head))   