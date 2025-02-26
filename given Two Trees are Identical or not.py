class Node:
    def __init__(self, key):
        self.key = key 
        self.left = None 
        self.right = None

def are_identical(root1, root2)        :
    if root1 is None and root2 is None:
        return True 
    
    if root1 is None or root2 is None :
        return False 
    
    return (root1.key == root2.key and 
            are_identical(root1.left, root2.left) and 
            are_identical(root1.right, root2.right))

if __name__ == "__main__":
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    
    if are_identical(root1, root2):
        print("The two trees are identical.")
    else:
        print("The two trees are not identical.")
