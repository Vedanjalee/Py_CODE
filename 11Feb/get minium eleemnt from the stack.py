class MinStack:

    def __init__(self):
        self.stack = []       
        self.min_stack = []   

   
    def push(self, val):
        self.stack.append(val)
        
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            top = self.stack.pop()
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    
    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None



min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
print("Minimum Element:", min_stack.getMin())  
min_stack.push(1)
print("Minimum Element:", min_stack.getMin()) 
min_stack.pop()
print("Minimum Element:", min_stack.getMin()) 

min_stack.pop()
print("Top Element:", min_stack.top())   
