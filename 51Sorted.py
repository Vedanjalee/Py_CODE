arr = [20, 23, 23, 45, 78, 88]
n = len(arr)
count = 0

for i in range(1,n):
    if arr[i] >=  arr[i-1]:
        count =0
    else:
        count = 1
        break
if count == 0:
    print("sorted")
else: 
    print("not sorted")            
