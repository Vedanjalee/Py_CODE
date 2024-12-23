A =[1,2,3,4,5,6,7,8,9]
target = 8

l,r =0, len(A)-1

while l<r :
    mid =(r+l) // 2
    if A[mid] == target :
        print(mid, target)
        break
    elif A[mid] < target:
        l = mid + 1    
    else: 
        r = mid -1

