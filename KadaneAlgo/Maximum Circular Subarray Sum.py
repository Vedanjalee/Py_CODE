def max_circular_subarray_sum(nums):
    def kadane(arr):
        max_sum = float('-inf')
        current_sum = 0 

        for num in arr:
            current_sum = max(num, current_sum + num )
            max_sum = max(max_sum, current_sum)
        return max_sum 

    max_normal = kadane(nums)
    if max_normal <0:
        return max_normal 

    total_sum  = sum(nums)
    min_subarray_sum   = kadane([-num for num in nums])

    max_circular = total_sum + min_subarray_sum 

    return max(max_normal ,  max_circular)  