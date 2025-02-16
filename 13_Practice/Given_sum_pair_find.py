def find_pair_with_sum_sorted(nums, target_sum):
    nums.sort() 

    left,right = 0,len(nums)-1 

    while left<=right:

        current_sum =  nums[left] + nums[right] 
        if current_sum == target_sum :
            return (nums[left], nums[right])
        elif current_sum < target_sum : 
            left += 1
        else:
            right -= 1
    return None              

nums = [10, 5, 2, 7, 8]
target_sum = 15
print(find_pair_with_sum_sorted(nums, target_sum))  
