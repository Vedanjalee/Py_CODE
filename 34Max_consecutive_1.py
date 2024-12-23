arr = [1, 1, 0, 1, 1,1, 1, 0, 1, 1]

max_count = 0
count = 0

for a in arr:
    if a==1:
        count += 1
       
    else:
        max_count =max (max_count, count)
        count = 0
print(max_count)            