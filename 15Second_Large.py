arr= [12, 35, 1, 10, 34, 1]
# Output: 34
lar = 0
sec =0
third =0

for i in range(len(arr)):
    if lar < arr[i]:
        lar = arr[i]

for i in range(len(arr)):
    if arr[i] != lar and sec<arr[i]:
       sec = arr[i]

for i in range(len(arr)):
    if arr[i] != lar and arr[i] != sec and arr[i] > third:
        third = arr[i]

print(lar,sec, third)


