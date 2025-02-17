class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        
        if not root:
            return True
        
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        return abs(leftHeight - rightHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


        return False

    def getHeight(self, root):
        
        if not root:
            return 0
        
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        
        return max(leftHeight, rightHeight) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

solution = Solution()

if solution.isBalanced(root):
    print("The tree is balanced.")
else:
    print("The tree is not balanced.")
                                