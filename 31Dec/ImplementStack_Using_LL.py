class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class Stack:
    def __init__(self):
        self.top = None  

    
    def push(self, x):
        new_node = Node(x)  
        new_node.next = self.top  
        self.top = new_node  
        print("Pushed onto the stack : ", x)

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        temp = self.top  
        self.top = self.top.next  
        print("Popped  from the stack.", temp.data)
        return temp.data

    def peek(self):
        if self.is_empty():
            print("Stack is empty! No top element.")
            return None
        return self.top.data  

    def is_empty(self):
        return self.top is None

    
    def print_stack(self):
        current = self.top
        if current is None:
            print("Stack is empty!")
            return
        print("Stack elements (top to bottom):", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.print_stack()  

print("Top element:", stack.peek())  

print("Popped element:", stack.pop())  
stack.print_stack()  

print("Is stack empty?", stack.is_empty())  
