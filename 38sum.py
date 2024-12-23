# arr = [1, 2, 3, 24]
# s =0
# for i in range(len(arr)):
#     s+= arr[i]
# print(s)    


# rev
arr = [1, 2, 3, 4]
l,r =0,len(arr)-1

while l<r :
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1
print(arr)    
