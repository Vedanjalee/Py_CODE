class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key) 

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    return root      

def search(root, key):
    if root is None or root.val == key:
        return root  
    
    if key < root.val:
        return search(root.left, key)
    
    return search(root.right, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 70)
insert(root, 20)
insert(root, 40)
insert(root, 60)
insert(root, 80)

print("Inorder traversal of the BST:")
inorder(root)
print("\n")


key = 40
if search(root, key):
    print(f"{key} found in BST")
else:
    print(f"{key} not found in BST")


key = 90
if search(root, key):
    print(f"{key} found in BST")
else:
    print(f"{key} not found in BST") 