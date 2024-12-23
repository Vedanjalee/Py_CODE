arr = [12, 34, 45, 9, 8, 90, 3]

even =[]
odd=[]

for i in range(len(arr)):
    if arr[i] %2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])

print(even + odd)            