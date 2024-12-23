arr = [1, 2,9, 4, 5]
# if arr == sorted(arr):
#     print("yes sorted")
# else:
#     print("not sorted")    
count = 0
for i in range(1,len(arr)):
    if arr[i-1] > arr[i]:
        count += 1
        break

if count == 1:
    print("not sorted")    
else:
    print("sorted")    