def Find_all_TargetSum_value_Pairs(nums, target_sum):
    nums.sort()
    left , right = 0 , len(nums) - 1
    result =[]
    while left<right :
        curr_sum = nums[left] + nums[right] 

        if curr_sum == target_sum : 
            result.append((nums[left], nums[right ]))
            left += 1
            right -= 1

        elif curr_sum< target_sum : 
            left += 1

        else:
            right -= 1
   
    return result                   





nums = [10,5,2,7,8,7]
target_sum = 15
print(Find_all_TargetSum_value_Pairs(nums, target_sum))