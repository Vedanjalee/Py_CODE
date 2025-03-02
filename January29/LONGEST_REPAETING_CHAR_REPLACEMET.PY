def characterReplacement(s,k):
    max_len = 0
    max_freq = 0
    count = {}
    left = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])

       
        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

s = "AABABABA"
k = 1
result = characterReplacement(s, k)
print("The length of the longest substring after k replacements is: ", result )
