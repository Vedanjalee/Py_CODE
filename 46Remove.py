arr = [10, 20, 30, 40, 50]
k = 2
# print(arr[:k] + arr[k+1:])
new =[]
for a in range(len(arr)):
    if a != k:
        new.append(arr[a])
    else:
        continue
print(arr)        
print(new)

