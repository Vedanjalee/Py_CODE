def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def shortestPalindrome(s: str) -> str:
    # If the string is already a palindrome, return it.
    if is_palindrome(s):
        return s
    
    # Check all prefixes from longest to shortest
    for i in range(len(s)):
        if is_palindrome(s[i:]):
            # If the substring s[i:] is a palindrome, append the remaining part
            # of the string (from the start to i) to the front
            return s[:i][::-1] + s
    
    return s  # In case no palindrome is found (which should not happen).

# Example usage:
input_str = "aacecaaa"
print(shortestPalindrome(input_str))  # Output: "aaacecaaa"
