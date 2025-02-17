class Node : 
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

def postorder(root, arr) :

    if root is None : 
        return 
    
    postorder(root.left, arr)
    postorder(root.right, arr)
    arr.append(root.val) 

def postOrder(root) :
    arr = [] 
    postorder(root, arr) 
    return arr 

def printList(lst) :
    for num in lst : 
        print(num, end = " ")
    print() 

root = Node(1)  
root.left = Node(2)  
root.right = Node(3)  
root.left.left = Node(4)  
root.left.right = Node(5)

result = postOrder(root) 

print("Postorder traversal: ", end = "")
printList(result)