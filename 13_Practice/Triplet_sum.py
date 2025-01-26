def triplet_sum (nums, target_sum):
    nums.sort()

    n = len(nums)

    for i in range(n-2):
        left, right = i+1, n-1 


        while left<right :
            current_sum = nums[i] + nums[left] +nums[right]

            if current_sum == target_sum :
                return (nums[i], nums[left], nums[right])
            
            elif current_sum< target_sum:
                left += 1

            else:
                right -= 1 
    return None       

nums = [1, 4, 6, 8, 10, 45]
target_sum = 22

result = triplet_sum(nums, target_sum)

if result :
    print("triplet fount ", result)

else:
    print("no triplet found ")