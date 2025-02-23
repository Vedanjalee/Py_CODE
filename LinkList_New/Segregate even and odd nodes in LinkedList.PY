class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self, new_data) :
        new_node = Node(new_data) 
        if not self.head :
            self.head = new_node 
            return 
        temp = self.head 
        while temp.next :
            temp = temp.next 
        temp.next = new_node 

    def segregate_even_odd (self):
        if not self.head or not self.head.next :
            return
        even_head= even_tail = None 
        odd_head = odd_tail = None 
        current = self.head 

        while current:
            next_node = current.next 
            current.next = None 

            if current.data %2 == 0:
                if even_head is None :
                    even_head  = even_tail = current 

                else:
                    even_tail.next = current 
                    even_tail = even_tail.next 

            else:
                if odd_head is None :
                    odd_head = odd_tail = current
                else:
                    odd_tail.next = current 
                    odd_tail = odd_tail.next 

            current = next_node 

        if not even_head :
            self.head = odd_head 
            return 

        if not odd_head :
            self.head =even_head 
            return 

        even_tail.next = odd_head 
        self.head = even_head 
                            
           
    def print_list(self):
        temp = self.head 
        while temp :
            print(temp.data, end =" -> ")
            temp = temp.next 
        print("None ")

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

print("Original Linked List:")                                   

llist.print_list() 

llist.segregate_even_odd()

print("LL after segregating even and odd nodes: ")

llist.print_list()
    
    