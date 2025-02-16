def longest_unique_substr(s) : 
    n = len(s)
    max_len = 0 

    for i in range(n) : 
        seen = set() 

        for j in range(i, n):

            if s[j] in seen : 
                break 
            seen.add(s[j])

            max_len = max(max_len , len(seen))

        return max_len
s = "abcabcbb"
print( longest_unique_substr(s))        
        
