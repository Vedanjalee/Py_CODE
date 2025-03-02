class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def areIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    #  left/right subtrees are identical or not
    return (root1.data == root2.data and
            areIdentical(root1.left, root2.left) and
            areIdentical(root1.right, root2.right))

# Function to check if root2 is a subtree of root1
def isSubtree(root1, root2):
    if root2 is None:
        return True
    if root1 is None:
        return False

    
    if areIdentical(root1, root2):
        return True

    # Recur for left and right subtrees of root1
    return isSubtree(root1.left, root2) or \
      isSubtree(root1.right, root2)

if __name__ == "__main__":
  
    # Construct Tree root1
    #          26
    #         /  \
    #        10   3
    #       / \    \
    #      4   6    3
    #       \
    #        30
    root1 = Node(26)
    root1.right = Node(3)
    root1.right.right = Node(3)
    root1.left = Node(10)
    root1.left.left = Node(4)
    root1.left.left.right = Node(30)
    root1.left.right = Node(6)

    # Construct Tree root2
    #          10
    #         /  \
    #        4    6
    #         \
    #          30
    root2 = Node(10)
    root2.right = Node(6)
    root2.left = Node(4)
    root2.left.right = Node(30)

    if isSubtree(root1, root2):
        print("true")
    else:
        print("false")
