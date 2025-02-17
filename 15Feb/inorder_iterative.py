class Node:
    def __init__(self, val):
        self.val= val
        self.left = None
        self.right = None


def inorder_iterative(root) : 
    stack =[] 
    inorder_list =[] 

    curr = root

    while stack or curr:
        while curr: 
            stack.append(curr) 
            curr = curr.left

        curr = stack.pop() 
        inorder_list.append(curr.val)

        curr = curr.right 
    return inorder_list

root = Node(1)   
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result_iterative =   inorder_iterative(root) 
print("inorder Traversal :", result_iterative )       