arr = [-10, -5, 0, 3, 7]
# Output: 3  
# Explanation: arr[3] == 3 

l,r = 0, len(arr)-1

while l<r:
    mid = (r+l)//2 
    if arr[mid] == mid:
        print(mid) 
        break
    elif arr[mid]> mid:
        r = mid -1 
    else: 
        l = mid + 1
