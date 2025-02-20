def kidsWithCandies(candies, extraCandies) :
    max_candy = max(candies) 
    return [candy + extraCandies >= max_candy for candy in candies]

print(kidsWithCandies([2, 3, 5, 1, 3], 3))
