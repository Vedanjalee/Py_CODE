from itertools import permutations

# permuation from itertools provide all the combinations of avaliable data

def largestNumber(nums):
    all_permutations = permutations(nums)  # Generate all possible orderings
    max_number = ""

    for perm in all_permutations:
        num_str = "".join(map(str, perm))  # tuple to string(so if there are large numbers it will also be retured ..........no number rage issue)
        max_number = max(max_number, num_str)   # Get lexicographically largest number
    
    return max_number


nums = [3, 30, 34, 5, 9]
print(largestNumber(nums))  # "9534330"
