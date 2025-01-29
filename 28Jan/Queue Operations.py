from collections import deque 

class Queue:
    def __init__(self):
        self.queue= deque() 

    def enqueue(self, x) :
        self.queue.append(x)

    def dequeue(self) -> int:
        return self.queue.popleft() if not self.empty() else -1


    def front(self) -> int:
        return self.queue[0] if not self.empty() else -1

    def rear(self) -> int:
        return self.queue[-1] if not self.empty() else -1


    def empty(self):
        return len(self.queue) == 0 
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Dequeued:", q.dequeue())  
print("Front:", q.front())       
print("Rear:", q.rear())         
print("Is empty:", q.empty())    
          