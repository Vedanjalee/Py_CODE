                            
def findContentChildren(greed, cookieSize) :
    n = len(greed)

    m = len(cookieSize)

    greed.sort()

    cookieSize.sort()

    l = 0

    r = 0

    while l < m and r < n:
        if greed[r] <= cookieSize[l]:
            r += 1
        l += 1
    return r


greed = [1, 5, 3, 3, 4]
cookieSize = [4, 2, 1, 2, 1, 3]
    
    
ans = findContentChildren(greed, cookieSize)
    
print("No. of kids assigned cookies:  ", ans)
                           
                        