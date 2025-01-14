def binary_search(nums,target):
    low,high = 0, len(nums)-1 

    while low<=high:

        mid = (low + high) //2

        if nums[mid] ==target:
            return mid
        
        elif nums[mid] <target :
            low = mid + 1
        else :
            high = mid - 1
    return -1        
nums = [1,2,5,6,7,89,90]
target = 5
print(binary_search(nums,target))                