def is_palindrome(s):
    return s == s[::-1]  

def min_deletes(s):
    n = len(s)
    max_palindrome_length = 1  

    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
       
            if is_palindrome(substring):
                max_palindrome_length = max(max_palindrome_length, len(substring))

    return n - max_palindrome_length



s1 = "aebcbda"
s2 = "geeksforgeeks"

print("Minimum deletions for '{s1}': {min_deletions_brute_force(s1)}")
print("Minimum deletions for '{s2}': {min_deletions_brute_force(s2)}")
