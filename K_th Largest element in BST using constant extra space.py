class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def kth_largest(root, k):
    if root is None :
        return -1 

    curr = root 
    cnt = 0 

    while curr is not None :
        if curr.right is None :
            cnt += 1

            if cnt == k:
                return curr.data 

            curr = curr.left

        else:
            succ = curr.right

            while succ.left is not None and succ.left != curr:
                succ = succ.left     

            if succ.left is None :
                succ.left = curr 
                curr = curr.right 
            else:
                succ.left = None 
                cnt += 1

                if cnt == k:
                    return curr.data 
                curr = curr.left 
    return -1                    


if __name__ == "__main__":

    # Create a hard-coded tree:
    #         20
    #       /   \
    #      8     22
    #    /  \
    #   4   12
    #      /  \
    #     10   14
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    k = 3

    print(kth_largest(root, k))
