from collections import defaultdict

def longest_substring_k_distinct(s, k):
    if not s or k == 0:
        return 0

    char_count = defaultdict(int)
    left = 0
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] += 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

s = "eceba"
k = 2
print("Longest Substring with At Most 2 Distinct Characters:", longest_substring_k_distinct(s, k))
