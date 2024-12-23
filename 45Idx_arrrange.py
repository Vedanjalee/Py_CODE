arr = [5, 8, 3, 2, 7, 6, 9, 1]
even_idx =[]
odd_idx =[]

for i in range(len(arr)):
    if i%2 == 0:
        even_idx.append(arr[i])
    else:
        odd_idx.append(arr[i])
even_idx.sort()
odd_idx.sort()

result = even_idx + odd_idx
print(result)