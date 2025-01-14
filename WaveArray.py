arr = [1, 3, 4, 2, 5, 6]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] >arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(0,len(arr)-1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)    