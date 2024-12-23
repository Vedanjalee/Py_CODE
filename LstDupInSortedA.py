arr= [1, 5, 5, 6, 6,7]

# Last index= 4
# Last duplicate item: 6

for i in range(len(arr)-1 , 0,-1):
    if arr[i] == arr[i-1]:
        print(i, arr[i])
        break    