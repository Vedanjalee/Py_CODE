def Move_zeroes_to_end(nums):
    j = 0 
    for i in range(len(nums)):
        if nums[i] != 0 :
            nums[i], nums[j] = nums[j] , nums[i] 
            j += 1
    return j, nums[:i+1]
nums = [1,3,0,30,9,0,0,0,9,0]
print(Move_zeroes_to_end(nums))
