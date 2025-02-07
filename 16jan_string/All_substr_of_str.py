def find_all_substr(s):

    substrings =[]

    for i in range(len(s)):
        for j in range(i+1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings 

s = "abc"
result = find_all_substr(s)
print("this are all the substrings : " , result) 

