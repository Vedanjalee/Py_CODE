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


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # 1,2. Node with one or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # Case 3: Node with two children
        temp = minValueNode(root.right)  
        root.val = temp.val 
        root.right = deleteNode(root.right, temp.val)  
    return root


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


print("Inorder traversal before deletion:")
inorder(root)
print("\n")


root = deleteNode(root, 50)


print("Inorder traversal after deletion:")
inorder(root)
print("\n")