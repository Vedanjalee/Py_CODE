def two_sum(nums, target):

    nums_map ={}

    for i ,nums in enumerate(nums):

        complement = target -nums

        if complement in nums_map :
            return [nums_map[complement],i] 
        
        nums_map[nums] = i 

print(two_sum([2,3,6,11,14],9))