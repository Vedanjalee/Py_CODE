def longest_repeating_substr(s) : 
    n = len(s) 
    max_len = 0 

    for i in range(n) :
        for j in range(i+1, n+1):

            substring = s[i:j] 
            if substring in s[j:]:
                max_len = max(max_len , len(substring))
    return max_len 

s = "banana"            
print(longest_repeating_substr(s) )
            