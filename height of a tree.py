# Python program to find the diameter
# of a binary tree.

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Function to compute the height 
# of a tree.
def height(root):
    
    if root is None:
        return 0


    return 1 + max(height(root.left), height(root.right))


def diameter(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)


    return max(lheight + rheight, ldiameter, rdiameter)

if __name__ == "__main__":
    
    # Constructed binary tree is
    #          5
    #        /   \
    #       8     6
    #      / \   /
    #     3   7 9
    
    root = Node(5)
    root.left = Node(8)
    root.right = Node(6)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(9)

    print(diameter(root))
