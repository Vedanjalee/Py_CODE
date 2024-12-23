arr = [3, 4,7,7, 7, 9, 99]
num = 7
res =-1
l,r =0, len(arr)-1

while l<= r:
    mid =(l+r)//2
    if arr[mid] == num:
        # res = mid 
        # l = mid +1 
        res = mid
        r = mid - 1

    elif arr[mid] < num: 
        l = mid + 1

    else: 
        r= mid - 1
print(res)            

