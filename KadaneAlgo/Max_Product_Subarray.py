def max_product_subarray(nums):
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    start = end = temp_start = 0 

    for i in range(1,len(nums)):
        if nums[i] < 0:
            max_product , min_product = min_product, max_product 
        
        if nums[i] > max_product*nums[i] :

            max_product =  nums[i]
            temp_start = i 

        else:
            max_product *= nums[i]

        min_product = min(nums[i] , min_product * nums[i])
        
        if max_product > result :
            result = max_product 
            start = temp_start 
            end = i 
        
    return result, nums[start:end + 1]        

nums = [2, 3, -2, 4]
ANS, subarray = max_product_subarray(nums)
print("Maximum Product:", ANS)
print("Subarray:", subarray)