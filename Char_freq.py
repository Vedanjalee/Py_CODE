def find_char_freq(s):
    freq ={}

    for char in s:
        if char in freq:
            freq[char] += 1 
        else:
            freq[char] = 1
    return freq 

s ="aabbgcc"
char_freq=    find_char_freq(s) 
print(char_freq)         