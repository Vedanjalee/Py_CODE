from collections import Counter

def min_window(s, t):
    
    if len(s) < len(t):
        return ""
    
    target_count = Counter(t)  
    window_count = Counter()  
    required = len(target_count)  
    new_formed = 0  
    
    left = 0  
    right = 0  
    min_length = float("inf")  
    min_window = ""  


    while right < len(s):
       
        char = s[right]
        window_count[char] += 1
        
       
        if char in target_count and window_count[char] == target_count[char]:
            new_formed += 1
        
       
        while left <= right and new_formed == required:
            char = s[left]
            
         
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = s[left:right+1]
            
           
            window_count[char] -= 1
            if char in target_count and window_count[char] < target_count[char]:
                new_formed -= 1
            
            left += 1
        
       
        right += 1
    
    return min_window


s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))  
