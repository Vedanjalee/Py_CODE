class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def invert_tree(root):
    if root is None:
        return None
    
    root.left, root.right = root.right , root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root

def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.key, end=" ")
        in_order_traversal(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("Original tree (in-order traversal):")
    in_order_traversal(root)
    
    root = invert_tree(root)
    
    print("\nMirrored tree (in-order traversal):")
    in_order_traversal(root)

