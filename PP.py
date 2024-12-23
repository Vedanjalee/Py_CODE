# arr = [64, 34, 25, 12, 22, 11, 90] 
# n = len(arr)
# for i in range(len(arr)):
#     for j in range(0, n-i-1):

#         if arr[j]> arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#             print(arr)        

# selection

# for i in range(len(arr)):
#     min_idx= i 
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_idx]:
#             min_idx = j
#     arr[min_idx], arr[i]=   arr[i], arr[min_idx] 
# print(arr)          
# 
# arr = [12, 3, 5, 7, 19]
# k = 2  
# arr.sort()
# print(arr[-k])

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr)//2 
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     sorted_arr = []

#     i=j = 0 

#     while i<len(left) and j<len(right):
#         if left[i] <= right[j]:
#             sorted_arr.append(left[i])
#             i += 1
#         else:
#             sorted_arr.append(right[j])
#             j += 1

#     sorted_arr.extend(left[i:])
#     sorted_arr.extend(right[j:])

#     return sorted_arr            

# arr = [38, 27, 43, 3, 9, 82, 10]
# print(arr)
# print(merge_sort(arr))

# arr =[12,4,2,6,9,43,5]
# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j]  > arr[j+1]:
#            arr[j+1],arr[j] = arr[j], arr[j+1]
# print(arr)
