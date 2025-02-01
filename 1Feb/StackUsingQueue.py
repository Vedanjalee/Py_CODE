class StackUsingTwoQueues:
    def __init__(self):
        self.q1 =[]
        self.q2 = []

    def push(self,data) :

        self.q2.append(data) 


        while self.q1 :
            self.q2.append(self.q1.pop(0))  

        self.q1 , self.q2 = self.q2, self.q1 

    def pop(self):
        if not self.q1 :
            return None 

        return self.q1.pop(0)

    def peek(self):

        if not self.q1:
            return None 
        return self.q1[0] 

    def is_empty(self):
        return len(self.q1) == 0 

stack = StackUsingTwoQueues()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  
print(stack.peek())  
print(stack.is_empty())  