class Queue:
    def __init__(self):
        self.queue = []  

    def enqueue(self,x):
        self.queue.append(x) 

    def dequeue(self) : 
        if not self.empty() :
            return  self.queue.pop(0) 
        return -1 
    
    def front(self):
        if not self.empty() :
            return self.queue[0] 
        return -1
    
    def empty(self):
        return len(self.queue) == 0 


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Dequeued:", q.dequeue())  # Output: 10
print("Front:", q.front())       # Output: 20
print("Is queue empty?", q.empty())  # Output: False
print("Dequeued:", q.dequeue())  # Output: 20
print("Dequeued:", q.dequeue())  # Output: 30
print("Is queue empty?", q.empty())  # Output: True
                    
