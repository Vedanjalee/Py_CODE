class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  


class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None        
   
    def enqueue(self, x):
        new_node = Node(x)  
        if self.rear is None:
            self.front = self.rear = new_node
        
        else:
            
            self.rear.next = new_node
            self.rear = new_node
        print("Enqueued to the  queue",x)

    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        temp = self.front  
        self.front = self.front.next 
        if self.front is None:
            self.rear = None  
        print("Dequeued from the queue:", temp.data)
        return temp.data


    def front_element(self):
        if self.is_empty():
            print("Queue is empty! No front element.")
            return None
        return self.front.data  

   
    def is_empty(self):
        return self.front is None

    
    def print_queue(self):
        current = self.front
        if current is None:
            print("Queue is empty!")
            return
        print("Queue elements:", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()



queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.print_queue()  

print("Front element:", queue.front_element())  

print("Dequeued element:", queue.dequeue())  
queue.print_queue()  

print("Is queue empty?", queue.is_empty()) 

queue.dequeue()
queue.dequeue()
queue.print_queue()