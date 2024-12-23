# arr =[11 ,8 ,5 ,7, 5 ,100]
# Output: 25 
# Explanation: The minimum product of any two numbers will be 5 * 5 = 25.
arr=[98, 76, 544, 123, 154 ,675 ]
arr.sort()
# O(n*log(n))---------Auxiliary space :O(1)

print(arr[0]*arr[1])  
# min_product = float('inf')

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] * arr[j] < min_product:
#             min_product = arr[i] * arr[j]
# print(min_product)            
