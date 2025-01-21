def increasing_Subsequence_triplets (nums):

    first = float('inf')
    second = float('inf')

    for num in nums:
        if num<= first:
            first= num
    
    
        elif num<=second :
            second = num 

    
        else:
            return  first , second, num
    return False


nums = [2, 1, 5, 0, 4, 6]

# nums = [1,2,3,4,5,0]
# nums = [5,4,3,2,1]
print(increasing_Subsequence_triplets (nums))
                                     

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.