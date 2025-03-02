
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def isSumProperty(root):

    # If root is None or it's a leaf node
    # then return true
    if root is None or (root.left is None and root.right is None):
        return 1

    sum = 0

    # If left child is not present then 0
    # is used as data of left child
    if root.left is not None:
        sum += root.left.data

    # If right child is not present then 0
    # is used as data of right child
    if root.right is not None:
        sum += root.right.data

    # if the node and both of its children
    # satisfy the property return 1 else 0
    return 1 if (root.data == sum
            and isSumProperty(root.left)
            and isSumProperty(root.right)) else 0

if __name__ == "__main__":
    
    # Create a hard coded tree.
    #         35
    #       /   \
    #      20    15
    #     /  \  /  \
    #   15   5 10   5
    root = Node(35)
    root.left = Node(20)
    root.right = Node(15)
    root.left.left = Node(15)
    root.left.right = Node(5)
    root.right.left = Node(10)
    root.right.right = Node(5)

    print(isSumProperty(root))
