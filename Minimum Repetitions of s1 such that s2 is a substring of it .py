def min_repetitions(s1, s2):
    repeats = 1
    concatenated = s1
    
    
    while len(concatenated) < len(s2) or s2 not in concatenated:
        concatenated += s1
        repeats += 1
        
        
        if len(concatenated) > 2 * len(s2) + len(s1):
            return -1

    return repeats


s1 = "abcd"
s2 = "cdabcdab"
print(min_repetitions(s1, s2))  # Output: 3
