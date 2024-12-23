arr=[10,12,11,20,4]
# Output: 20

lar = 0
for i in range(len(arr)):
    if lar < arr[i]:
        lar = arr[i]
print(lar)        