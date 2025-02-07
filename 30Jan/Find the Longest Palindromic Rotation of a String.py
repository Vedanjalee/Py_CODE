def longest_palindromic_rotation(s):
    n = len(s)
    max_palindrome = ""

    for i in range(n):
        rotated = s[i:] + s[:i]
        if rotated == rotated[::-1] and len(rotated) > len(max_palindrome):
            max_palindrome = rotated

    
    if max_palindrome:
        return max_palindrome
    else:
        return "No palindromic rotation"


s = "racecar"
print("Longest Palindromic Rotation:", longest_palindromic_rotation(s))
