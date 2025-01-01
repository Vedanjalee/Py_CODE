class Queue:
    def __init__(self):
        self.queue =[]

    def enqueue(self,x):
        self.queue.append(x)
        print("enqueued to the queue: ", x)

    def dequeue(self  ):
        if self.is_empty():
            print("queue is empty! Cannot dequeue")
            return None 
        return self.queue.pop(0)  
    
    def front(self):
        if self.is_empty():
            print("Queue is empty! No front element.")
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def print_queue(self):
        print("Queue elements:", self.queue)

my_queue = Queue()

   
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.print_queue()  

    
print("Front element:", my_queue.front())  

print("Dequeued element:", my_queue.dequeue())  
my_queue.print_queue()  

    
print("Is queue empty?", my_queue.is_empty())  

print("Queue size:", my_queue.size())     
