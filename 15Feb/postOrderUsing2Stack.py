class Node : 

    def __init__(self, val) : 
        self.val = val 
        self.left = None
        self.right = None

def postOrder(root):
    postorder =[] 

    if root is None :
        return postorder 
    
    st1, st2 =[],[] 

    st1.append(root)
    while st1 :
        node = st1.pop() 
        st2.append(node)

        if node.left: 
            st1.append(node.left)

        if node.right: 
            st1.append(node.right)

    while st2:
        postorder.append(st2.pop().val) 
    return postorder 


def printList(lst) :
    for num in lst : 
        print(num, end=" ")
    print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result = postOrder(root)

print("Postorder traversal:", end=" ")
printList(result)

