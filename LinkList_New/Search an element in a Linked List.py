class Node :
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 

def search_ele_in_LL(head,target):

    temp = head 
    while temp is not None :
        if temp.data ==    target:
            return 1
        temp = temp.next
    return 0 

if __name__ == "__main__":

    arr = [1,2,3]
    head = Node (arr[0])
    head.next = Node(arr[0])
    head.next.next = Node(arr[2])

    val =3 
    print(search_ele_in_LL(head, val))
