def count_distinct_substrings(s):
    n = len(s)
    substrings = set()

    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(s[i:j])
    
    return len(substrings)

s = "abc"
print("Number of Distinct Substrings:", count_distinct_substrings(s))
