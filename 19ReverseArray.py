arr= [1,2,3,4]
l,r =0,len(arr)-1
while l<r:
    
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r-= 1
print(arr)    

# for i in range(len(arr)-1, -1,-1):
#     print(arr)