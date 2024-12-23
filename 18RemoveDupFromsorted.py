arr= [1, 2, 2, 3, 4, 4, 4, 5, 5]

# [1, 2, 3, 4, 5]

# seen = set()

i = 0
for j in range (1,len(arr)):
    if arr[j] != arr[i] :
        i += 1 
        arr[i] = arr[j]
        
print(arr[: i+1])

