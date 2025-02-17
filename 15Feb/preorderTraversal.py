class TreeNode: 

    def __init__(self,val) :

        self.val = val
        self.left =None 
        self.right = None 

class Solution: 
    def preorderTraversal(self, root):
        preorder =[]

        if root is None: 
            return preorder 
        
        stack =[root] 
        while stack:
            node = stack.pop() 

            preorder.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left: 
                stack.append(node.left)
        return preorder 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)              

sol = Solution() 
result = sol.preorderTraversal(root) 

print("preorder Traversal: ", result )

