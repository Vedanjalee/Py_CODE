class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        preorder = []
        if root is None:
            return preorder
        
        def traverse(node):
            if node:
                preorder.append(node.val)
                traverse(node.left)
                traverse(node.right)
        
        traverse(root)
        return preorder

def printList(lst):
    for num in lst:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    solution = Solution()
    result = solution.preorderTraversal(root)
    
    print("Preorder Traversal:")
    printList(result)
