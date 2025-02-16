def sorted_squares(nums):
    """
    Return the sorted squares of a sorted array.

    Args:
    nums: List[int] - A sorted array of integers.

    Returns:
    List[int] - A sorted array of the squares of the input integers.
    """
    # Initialize two pointers and an empty result list
    left, right = 0, len(nums) - 1
    result = []

    # Use a two-pointer approach to add the larger square first
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1

    # Reverse the result as it is constructed in descending order
    return result[::-1]


# Example usage
nums = [-4, -2, 0, 3, 5]

print("Input array:", nums)

# Call the function to get sorted squares
squared_result = sorted_squares(nums)
print("Sorted squares:", squared_result)
