arr =[10, 20, 10, 5, 15]
prefix =[0] * len(arr)
prefix[0] = arr[0]

for i in range(1,len(arr)):
    prefix[i] = prefix[i-1] + arr[i]
print(prefix)    
 
