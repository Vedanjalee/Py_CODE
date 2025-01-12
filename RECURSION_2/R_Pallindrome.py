def is_pallindrome(s):
    if len(s) <= 1:
        return True 
    
    if s[0] != s[-1]:
        return False
    
    return is_pallindrome(s[1:-1])

s = "MADM"
print(is_pallindrome(s))