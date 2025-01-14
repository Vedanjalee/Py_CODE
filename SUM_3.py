def threeSum(nums):
    nums.sort() 
    n = len(nums) 
    result = []

    for i in range(n):
        if i> 0 and nums[i] == nums[i+1] 
            continue 

        left , right = i+1, n - 1

        while left< right :
            total = nums[i] + nums[left] + nums[right] 

            if total ==0:
                result.append([nums[i], nums[left] , nums[right] ] ) 

                while left<right and nums[right] 


nums = [-1, 0, 1, 2, -1, -4]
w = threeSum(nums) 
print(w)

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
