def longest_common_prefix(strings):

    if not strings:
        return ""
    
    smallest_str = strings[0]
    for s in strings[1:]:
        if len(s) < len(smallest_str):
            smallest_str = s 

    for s in strings : 
        i = 0

        while i < len(smallest_str) and i < len(s) and smallest_str[i] == s[i]:
            i += 1

        smallest_str = smallest_str[:i]

        if not smallest_str : 
            return ""

    return smallest_str 

strings = ["flower", "flow", "flight"] 
result = longest_common_prefix(strings)
print("Longest Common Prefix:", result)
