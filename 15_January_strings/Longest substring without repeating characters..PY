def LongestSubStr_Length (s):
    char_set = set() 
    left   = 0 
    max_length = 0 

    for right in range(len(s)):

        while s[right] in char_set:
           
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


s1 = "abcabcbb"
print("Longest substring without repeating characters in ", s1,  LongestSubStr_Length (s1))  # Output: 3

s2 = "bbbbb"
print("Longest substring without repeating characters in" , s2,  LongestSubStr_Length (s2))    

s3 = "pwwkew"
print("Longest substring without repeating characters in " , s3,  LongestSubStr_Length (s3)) 