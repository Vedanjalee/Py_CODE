def subsequences(s, i, current):
    
    if i == len(s):
        print(current)  
        return

    
    subsequences(s, i + 1, current + s[i])

    subsequences(s, i + 1, current)

s = "abc"
print("Subsequences of", s)
subsequences(s, 0, "")
