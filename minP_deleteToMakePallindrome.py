def min_deletions(s, left, right):
    if left >= right:
        return 0
    if s[left] == s[right]:
        return min_deletions(s, left + 1, right - 1)
    return 1 + min(min_deletions(s, left + 1, right), 
                   min_deletions(s, left, right - 1))

def min_deletions_to_make_palindrome(s):
    return min_deletions(s, 0, len(s) - 1)

s = "abca"
print(min_deletions_to_make_palindrome(s))  # Output: 1
