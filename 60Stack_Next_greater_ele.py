def next_greater_element(arr):
    stack =[]
    result = [-1] * len(arr)  # Initialize result with -1
    
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    
    return result

# Test
nums = [4, 5, 2, 10, 8]
print("Original array:", nums)
print("Next greater elements:", next_greater_element(nums))



nums = [4, 5, 2, 10, 8]
print("Original array:", nums)
print("Next greater elements:", next_greater_element(nums))