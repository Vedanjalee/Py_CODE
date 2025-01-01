class Stack:
    def __init__(self):
        self.stack =[]

    def push(self,x):
        self.stack.append(x)
        print("pushed on stack: ", x)

    def pop(self):
        if self.is_empty():
            print("Stack is empty! can't pop")
            return None 
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            print("stack is empty ! No top element")
            return None 
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0 

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print("Stack elements", self.stack)

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.print_stack()

print("Top element:", my_stack.top())

print("Popped element:", my_stack.pop()) 
my_stack.print_stack() 

print("Is stack empty?", my_stack.is_empty())

print("Stack size:", my_stack.size()) 