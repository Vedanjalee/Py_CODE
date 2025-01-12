class Node :
    def __init__(self,data):
        self.data = data
        self.next = None 

class SLL:
    # def __init__(self):
    #     self.head = None 

    def ArrayToLL(self,arr):
        if not arr:
            return None 

        head = Node(arr[0])
        current= head 

        for value in arr[1:]:
            current.next = Node(value)
            current = current.next 
        return head 
    
    def print_display(self, head):
        current = head 
        while current :
            print(current.value, end =" ")
            current = current.next 
        print("None")  # Indicate the end of the list

# Example usage
arr = [10, 20, 30, 40]
ll = SLL()
ll.ArrayToLL(arr)
ll.print_display(self)