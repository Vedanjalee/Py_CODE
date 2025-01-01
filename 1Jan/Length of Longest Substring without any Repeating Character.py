def lengthOfLongest_Substr_without_repeat_value(s):
    All_Possible_Ascii_values= [-1] * 256

    left =0
    right = 0
    n = len(s)
    length = 0 

    while right<n:
        if All_Possible_Ascii_values[ord(s[right])] != -1:
            left = max(All_Possible_Ascii_values[ord(s[right])] + 1, left)
        All_Possible_Ascii_values[ord(s[right])] = right 

        length = max(length, right - left + 1)
        right += 1
    return length

# s = "takeUforward"

s = "abcdabcdba"
print(lengthOfLongest_Substr_without_repeat_value(s))       