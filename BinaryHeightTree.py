class Node :
    def __init__(self,key):
        self.key = key 
        self.left = None 
        self.right = None

def height(root):
    if root is None :
        return -1 
    
    lHeight = height(root.left)
    rHeight = height(root.right)

    return max(lHeight, rHeight) + 1

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    print("Height of the tree:", height(root))

