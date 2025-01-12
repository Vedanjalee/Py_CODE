

def B_search(arr, s, e ,target):
    if s>e:
        return -1 
    
    mid = s+(e-s) //2

    if  target == arr[mid]:
        return mid 
    
    if target < arr[mid] :
        return B_search(arr, s, mid-1 ,target)
    
    if target > arr[mid] :
        return B_search(arr, mid+1 , e ,target)

    
arr = [1,2,3,46,78,90]
target = 4
result = B_search(arr, 0, len(arr) - 1, target)
print(result, " is the index where target is found")