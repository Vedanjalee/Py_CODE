def is_palindrome(s):
    return s == s[::-1]

def shortest_palindrome(s):
    if not s:
        return s
    
    n = len(s)
    
    for i in range(n, -1, -1):
        if is_palindrome(s[:i]):
            suffix = s[i:]
            return suffix[::-1] + s  

s1 = "abcd"
print(shortest_palindrome(s1))

s2 = "aacecaaa"
print(shortest_palindrome(s2))
