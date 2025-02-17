class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def pre_in_post_traversal(root):
    
    pre, in_order, post = [], [], []

    if root is None:
        return []

    stack = [(root, 1)]

    while stack:
        node, state = stack.pop()

        if state == 1:
            pre.append(node.data) 
            stack.append((node, 2)) 

            if node.left:
                stack.append((node.left, 1))

        
        elif state == 2:
            in_order.append(node.data)  
            stack.append((node, 3))  

            if node.right:
                stack.append((node.right, 1))

        
        else:
            post.append(node.data)  

    return [pre, in_order, post]


def print_list(lst):
    print(" ".join(map(str, lst)))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

pre, in_order, post = pre_in_post_traversal(root)


print("Preorder traversal:", end=" ")
print_list(pre)

print("Inorder traversal:", end=" ")
print_list(in_order)

print("Postorder traversal:", end=" ")
print_list(post)
