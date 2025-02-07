def is_palindrome(s):
    return s == s[::-1]

def is_circular_palindrome(s):
    n = len(s)
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_palindrome(rotated):
            return True
    return False

s = "bba"
print("Is Circular Palindrome?", is_circular_palindrome(s))
