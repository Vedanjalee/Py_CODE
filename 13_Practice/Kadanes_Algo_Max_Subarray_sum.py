def max_subarray_sum(arr):

    curr_max = arr[0]
    total_max = arr[0]

    for i in range(1,len(arr)):

        curr_max = max(arr[i], arr[i]+curr_max)

        total_max = max(total_max, curr_max)

    return total_max 

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  
result = max_subarray_sum(arr)
print("Maximum subarray sum:", result)    
