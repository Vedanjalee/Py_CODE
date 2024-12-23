arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1], arr[j] 
# print(arr)            

frequency = {}
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

sorted_frequency = sorted(arr, key=lambda x: (-frequency[x], arr.index(x)))
print("Frequency in Descending Order:", sorted_frequency)