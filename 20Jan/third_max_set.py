def thirdMax( nums):
        max_set = set()
        for num in nums:
            max_set.add(num)

            if len(max_set)> 3:
                max_set.remove(min(max_set))

        if len(max_set) < 3:
            return max(max_set)
        return min(max_set) 
nums = list(map(int, input("Enter a list of integers: ").split()))


print("The third maximum number is:", thirdMax(nums))