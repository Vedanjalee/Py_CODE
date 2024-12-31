from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x) :
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) :
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self) :
        return not self.queue


obj = MyStack()
print("Push 1:")
obj.push(1)
print("Push 2:")
obj.push(2)
print("Current Top:", obj.top())  
print("Pop Element:", obj.pop())  
print("Is Empty?", obj.empty())  
print("Current Top:", obj.top())  
print("Pop Element:", obj.pop())  
print("Is Empty?", obj.empty())  

