class Node:
    def __init__(self, data , next=None):
        self.data = data 
        self.next = next 

def find_len_of_linkList(head):
    count =0
    temp = head 

    while temp is not None :
        temp = temp.next 
        count += 1
    
    return count 

def main() :
    arr =[2,3,4,5]
    head = Node(arr[0])
    temp = head 

    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next 
    print("Length of the linked list:", find_len_of_linkList(head))

main()