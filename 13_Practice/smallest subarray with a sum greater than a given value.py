# def smallest_subarray(nums, target_sum ):
#     n = len(nums)
#     current_sum = 0 
#     min_len = float ('inf')
#     start = 0 

#     for last in range(n):
#         current_sum += nums[last]

#         while current_sum > target_sum :
#             min_len = min(min_len, last - start + 1)
#             current_sum -= nums[start]
#             start += 1
#     return min_len

# nums = [1, 4, 45, 6, 0, 19]
# target_sum = 51
# result = smallest_subarray(nums, target_sum)

# if result:
#     print(f"The smallest subarray length is: {result}")
# else:
#     print("No such subarray exists.")
