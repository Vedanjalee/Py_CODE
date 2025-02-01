class Node :
    def __init__(self,data):
        self.data = data 
        self.children = []

    def add_child(self,child):
        self.children.append(child)

    def display(self, level = 0):
        print(" " * level * 4 + str(self.data))

        for child in self.children:
            child.display(level + 1)

root = Node("Root")
child1 = Node("Child1")
child2 = Node("Child2")

root.add_child(child1)
root.add_child(child2)

child1.add_child(Node("Child1.1"))
child1.add_child(Node("Child1.2"))

child2.add_child(Node("Child2.1"))                 

root.display()                