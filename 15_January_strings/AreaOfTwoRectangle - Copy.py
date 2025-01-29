class Rectangle : 
    def __init__(self, length , breadth ):
        self.length = length 
        self.breadth = breadth 

    def Area(self):
        return self.length * self.breadth 

rect1 = Rectangle(4, 5)  
rect2 = Rectangle(5, 8)  

print("area of rectangle 1 : ",rect1.Area())
print("area of rectangle 1 : ",rect2.Area())