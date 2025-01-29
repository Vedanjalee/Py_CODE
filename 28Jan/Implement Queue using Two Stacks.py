class QueueUsingStacks:
    def __init__(self):
        self.stack1 = [] 
        self.stack2 = [] 

    def enqueue(self,x):
        self.stack1.append(x)

    def dequeue(self): 
        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop()) 

        return self.stack2.pop() if self.stack2 else -1 

    def front (self) :

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop()) 
        return self.stack2[-1] if self.stack2 else -1 

    def empty(self):
        return not(self.stack1 or self.stack2)


queue = QueueUsingStacks()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Dequeued:", queue.dequeue())  # Output: 10
print("Front element:", queue.front())  # Output: 20
print("Is queue empty?", queue.empty())  # Output: False
