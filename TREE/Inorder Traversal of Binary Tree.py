class Node:
    def __init__(self, val):
       
        self.data = val
       
        self.left = None
        self.right = None

def inorder_traversal(root, arr):
    if not root:
        return
    inorder_traversal(root.left, arr)
    arr.append(root.data)
    inorder_traversal(root.right, arr)


def get_inorder(root):
    arr = []
    inorder_traversal(root, arr)
    return arr


root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


result = get_inorder(root)


print("Preorder Traversal:", end=" ")
   
for val in result:
    print(val, end=" ")
print()