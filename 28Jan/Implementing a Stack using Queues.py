from collections import deque 

class StackUsingQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)    

        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) : 
        if not self.empty() :
            return self.queue.popleft() 
        return -1 

    def top(self):
        if not self.empty():
            return self.queue[0] 
        return - 1

    def empty (self) : 
        return len(self.queue) == 0  


stack = StackUsingQueue()
stack.push(10)
stack.push(20)
stack.push(30)
print(f"Top element: {stack.top()}")  # Output: 30
print(f"Popped element: {stack.pop()}")  # Output: 30
print(f"Top element after pop: {stack.top()}")  # Output: 20
print(f"Is stack empty? {stack.empty()}")  # Output: False           