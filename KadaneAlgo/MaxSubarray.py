def MaxSubarray(arr):
    max_sum = arr[0]
    curr_sum = arr[0]

    for i in range(1, len(arr)):
        curr_sum = max(curr_sum , curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum 
arr = [2, 3, -2, 4]
print(MaxSubarray(arr))    