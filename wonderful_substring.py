def wonderfulstring(s):
    char_count = {} 
    
    left = 0 
    result = 0 

    for right in range(len(s)):

        while s[right] in char_count and char_count[s[right]]>0:
            char_count[s[left]] -= 1
            left += 1

        result += (right - left+1)

        if s[right] in char_count :
            char_count[s[right]] += 1 
        
        else:
            char_count[s[right]]    = 1
    return result   

s = "abcabc"
print("Number of wonderful substrings:", wonderfulstring(s))     

