def has_repeating_substrings(s, length):
    seen = set() 
    for i in range(len(s) - length + 1):
        substring = s[i: i+length]
        if substring in seen :
            return True 
        
        seen.add(substring)
    return False 

def longest_repeating_substring (s):
    l, r = 1, len(s)
    result = ""

    while l<=r :
        mid = (l+r) // 2

        if has_repeating_substrings(s,mid):   
            result = mid 

            l = mid + 1 
        else:
            r = mid -1
    return result 
s = "banana"
result = longest_repeating_substring(s)
print("The longest repeating substring is: ",result)             