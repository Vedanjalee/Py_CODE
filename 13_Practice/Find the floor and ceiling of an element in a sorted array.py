def find_floor_ceiling(nums, target):
    low, high = 0, len(nums)-1 

    floor = None
    ceiling = None 

    while low <= high:
        mid = (low+high)//2 

        if nums[mid] == target:
            return target,target 
        
        elif nums[mid] < target :
            floor = nums[mid] 
            low = mid + 1 
        else:
            ceiling = nums[mid]
            high = mid - 1
    return floor, ceiling 
nums = [1, 3, 5, 7, 9, 11]
target = 6
print(find_floor_ceiling(nums, target))           