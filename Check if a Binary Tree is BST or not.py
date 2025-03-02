class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def inorder(root, prev):
    if root is None:
        return True

    if not inorder(root.left, prev):
        return False

    if prev[0] >= root.data:
        return False

    prev[0] = root.data

    return inorder(root.right, prev)

def isBST(root):
    prev = [float('-inf')]
    return inorder(root, prev)




if __name__ == "__main__":
  
    # Create a sample binary tree
    #     10
    #    /  \
    #   5    20
    #        / \
    #       9   25

    root = Node(10)
    root.left = Node(5)
    # root.left.left = Node(3)
    # root.left.right = Node(7)
    root.right = Node(20)
    root.right.left = Node(9)
    root.right.right = Node(25)

    if isBST(root):
        print("True")
    else:
        print("False")
