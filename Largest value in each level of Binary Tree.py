
def helper (res, root, d):

    if(not root) :
        return 
    
    if (d==len(res)):
        res.append(root.val)

    else:

        res[d] = max(res[d] , root.val)  

    helper(res, root.left , d+1) 
    helper(res, root.right , d+1)

def largestValues(root) :
    res =[] 
    helper(res, root, 0) 
    return res 

class newNode:

    def __init__(self, data):
        self.val = data 
        self.left = None 
        self.right = None 

if __name__ == '__main__':
    """ Let us construct the following Tree
        4 
        / \ 
        9 2 
    / \ \
    3 5 7 """
    root = newNode(4) 
    root.left = newNode(9) 
    root.right = newNode(2) 
    root.left.left = newNode(3)
    root.left.right = newNode(5)
    root.right.right = newNode(7)
    print(*largestValues(root))                

