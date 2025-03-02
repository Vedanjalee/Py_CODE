# Sorted Array to BST

class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

# RECURSIVE FUNCTION TO CONSTRUCT BST 

def sortedArrayToBSTRecur(arr, start, end):
    if start> end :
        return None 
    
    mid = start + (end-start) //2
    root = Node(arr[mid])
    root.left = sortedArrayToBSTRecur(arr, start, mid-1)
    root.right = sortedArrayToBSTRecur(arr, mid+1, end)

    return root 

def sortedArrayToBST(arr) :
    return sortedArrayToBSTRecur(arr, 0 , len(arr) - 1)

def preOrder(root) :
    if root is None:
        return 
    
    print(root.data , end =" ")
    preOrder(root.left)
    preOrder(root.right)

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    root = sortedArrayToBST(arr)
    preOrder(root)

    
