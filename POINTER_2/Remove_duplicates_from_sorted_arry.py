def Remove_duplicates_from_sorted_array(nums):
    
    if not nums:
        return 0 ,[] 
    
    i = 0 
    for j in range(1,len(nums)):
        if nums[j] != nums[i] :
            i += 1
            nums[i] = nums[j] 
    return i+1, nums[:i+1]
    


nums = [1,2,2,3,4,5,6,7,7,8]
print(Remove_duplicates_from_sorted_array(nums))
