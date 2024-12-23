arr = [1, 3, 2, 2, 1]
# Output : 1 2 3
n=len(arr)
arr.sort()
new =[]
for i in range(n):
    if arr[i] != arr[i-1]:
        new.append(arr[i])
    else: 
        continue
print(arr, new)        

 

