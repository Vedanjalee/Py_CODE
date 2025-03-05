def is_palindrome(s):
    return s == s[::-1]

def min_repetitions_to_form_palindrome(s1, s2):
    repeats = 1
    concatenated = s1

    while len(concatenated) < len(s2) or s2 not in concatenated:
        concatenated += s1
        repeats += 1
        
        # ?? s2 appears as a palindrome
        if s2 in concatenated and is_palindrome(s2):
            return repeats
        
        # If length exceeds the expected/allowed limit, return -1
        if len(concatenated) > 2 * len(s2) + len(s1):
            return -1

    return repeats if is_palindrome(s2) else -1


s1 = "ab"
s2 = "baab"
print(min_repetitions_to_form_palindrome(s1, s2))  # Output: 2
