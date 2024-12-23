class Stack:
    def __init__(self):
        self.stack =[]

    # Push Operation    
    def push(self,value):
        self.stack.append(value)

        # Pop Operatin
    def pop(self):
        if self.is_empty():
            print("stack underflow! Cannot pop.")
            return None
        return self.stack.pop()    
    
    # Peek Operation
    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return None
        return self.stack[-1]
    
    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    
    # Stack size 
    def size(self):
        return len(self.stack)

# Using the Stack class
stack = Stack()
stack.push(5)
stack.push(15)
stack.push(25)

print("Top element:", stack.peek())  # Output: 25
print("Stack size:", stack.size())  # Output: 3

stack.pop()
print("After pop, top element:", stack.peek())  # Output: 15
print("Is stack empty?", stack.is_empty())  # Output: False    
