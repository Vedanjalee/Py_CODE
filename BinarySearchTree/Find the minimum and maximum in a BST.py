class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# insert a node in BST
def insert(root, key):
    if root is None:
        return Node(key)
    
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    return root


def findMin(root):
    if root is None:
        return None  
    
    while root.left is not None:
        root = root.left
    return root.val


def findMax(root):
    if root is None:
        return None 
    
    while root.right is not None:
        root = root.right
    return root.val


root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 70)
insert(root, 20)
insert(root, 40)
insert(root, 60)
insert(root, 80)


print(f"Minimum value in BST: {findMin(root)}")
print(f"Maximum value in BST: {findMax(root)}")
