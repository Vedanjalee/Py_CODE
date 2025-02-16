class Node:
    def __init__(self, val):
      
        self.data = val
        self.left = None
        self.right = None

def postorder_traversal(root, arr):
    if not root:
        return
  
    postorder_traversal(root.left, arr)
  
    postorder_traversal(root.right, arr)
  
    arr.append(root.data)


def get_postorder(root):
    arr = []
    postorder_traversal(root, arr)
    return arr

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result = get_postorder(root)

for val in result:
    print(val, end=" ")
print()