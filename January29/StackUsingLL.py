class Node:
    def __init__(self,data):
        self.data = data 
        self.next = next;

class Stack:
    def __init__(self):
        self.top = None 

    def push(self,data):
        node = Node(data) 
        node.next = self.top
        self.top = node 

    def pop(self):
        if self.top is None:
            print("stack is empty")
            return 
        print("popped", self.top.data) 
        self.top = self.top.next 

    def peek(self):
        if self.top is None :
            print("stack is empty") 
        else:
            print("top ele", self.top.data) 

stack = Stack()
stack.push(10)
stack.push(20)
stack.peek()
stack.pop()
stack.peek()                          