arr = [1, 2, 2, 3, 4, 4]
 
seen ={}

dup =[]

for num in arr:
    if num in seen:
        seen[num] += 1
    else:
        seen[num] = 1

for num, count in seen.items():
    if count > 1:
        dup.append(num)

print(dup)