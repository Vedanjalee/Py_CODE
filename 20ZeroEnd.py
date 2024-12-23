arr=[1, 2, 0, 4, 3, 0, 5, 0]
non_zero_i = 0

for i in range(len(arr)):
    if arr[i] >0:
        arr[i] , arr[non_zero_i] = arr[non_zero_i], arr[i]
        
       
        non_zero_i += 1
print(arr)  




