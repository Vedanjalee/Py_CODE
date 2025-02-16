def longestPallindromicSubstr(s):
    def expand_from_center(l,r):
        while l >= 0 and r<len(s) and s[l] == s[r] :
            l -= 1
            r += 1

        return s[l + 1: r]

    if len(s) == 0:
        return " "

    longest = " "

    for i in range(len(s)):
        odd_pallindrome = expand_from_center(i,i)
        even_pallindrome = expand_from_center(i,i+1)

        longest = max(longest, odd_pallindrome , even_pallindrome , key = len) 
    return longest 

s = "bab" 
print(longestPallindromicSubstr(s))      