from collections import Counter

def minWindow(S, T):

    if not S or not T:
        return ""
    
    char_count = Counter(T)
    
    min_len = float("inf")
   
    min_window = ""

    for left in range(len(S)):
    
        for right in range(left, len(S)):
          
            substring = S[left: right + 1]


            if containsAllChars(substring, char_count):
                
                if len(substring) < min_len :
                  
                    min_len = len(substring)
                 
                    min_window = substring 
   
    return min_window 

def containsAllChars(substring, char_count):
    
    sub_count = Counter(substring)
    
    for char in char_count : 
        
        if sub_count[char] < char_count[char] :
            return False 
  
    return True 

S = "ADOBECODEBANC"
T = "ABC"
print(minWindow(S, T))                      