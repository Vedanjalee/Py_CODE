def longest_consecutive_subsequence(arr):
    if not arr:
        return 0
    num_set = set(arr)
    longest_streak = 0 

    for num in  num_set :
        if num-1 not in num_set:
            curr_num = num 
            curr_streak = 1

            while curr_num + 1 in num_set :
                curr_num += 1 
                curr_streak += 1 
            longest_streak = max(longest_streak, curr_streak)
    return longest_streak 

arr = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_subsequence(arr)
print("Length of longest consecutive subsequence:", result)
            
