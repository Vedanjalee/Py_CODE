class Node :
    def __init__(self, data1, next1 = None ):
        self.data = data1
        self.next = next1 

    def mergeTwoSortedLinkedLists(list1, list2):     
        dummyNode = Node (-1) 
        temp = dummyNode 

        while list1 is not None and list2 is not None:
            if list1.data <= list2.data : 
                temp.next = list1 
                list1 = list1.next 
            else : 
                temp.next = list2 
                list2 = list2.next  

            temp = temp.next 


        if list1 is not None : 
            temp.next  = list1 
        else:
            temp.next = list2

        return dummyNode.next 


    def findMiddle(head) :

        if head is None or head.next is None : 
            return head 

        slow = head 
        fast = head.next 

        while fast is not None and fast.next is not None :
            slow = slow.next 
            fast = fast.next.next 
        return slow 


    def sortLL(head) :
        if head is None or head.next  is None:
            return head 

        middle = findMiddle(head)  

        right = middle.next
        middle.next = None 
        left = head 

        # Recursive sort left nd right 

        left = sortLL(left)
        right = sortLL(right)

        return  mergeTwoSortedLinkedLists(left, right)
    
def printLinkedList(head):
    temp = head
    while temp is not None:
        # Print the data of the current node
        print(temp.data, end=" ")
        # Move to the next node
        temp = temp.next
    print()

# Linked List: 3 2 5 4 1
head = Node(3)
head.next = Node(2)
head.next.next = Node(5)
head.next.next.next = Node(4)
head.next.next.next.next = Node(1)

print("Original Linked List: ", end="")
printLinkedList(head)

# Sort the linked list
head = sortLL(head)

print("Sorted Linked List: ", end="")
printLinkedList(head)



