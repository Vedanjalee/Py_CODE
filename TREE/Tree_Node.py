class Node:
    def __init__(self, val):
       
        self.data = val
       
        self.left = None
        self.right = None


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.right = Node(5)


def preorder_traversal(node):
    if node:
    
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


preorder_traversal(root)
