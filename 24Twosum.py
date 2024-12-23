arr = [0, -1, 2, -3, 1]
target = -2

# lst = []
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i] + arr[j] == target: 
#             lst.append([arr[i], arr[j]])
# print(lst)            

arr.sort()
l,r = 0, len(arr)-1
while l<r:
    sum = arr[l] + arr[r]

    if sum == target :
        print(arr[l], arr[r])
        break
    elif sum< target: 
        l += 1
    else: 
        r -= 1        

