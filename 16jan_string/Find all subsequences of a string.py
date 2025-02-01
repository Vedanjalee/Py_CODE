def subsequence_recursion(idx, curr, s, res):

    if idx == len(s):
        res.append(curr)
        return 
    
    subsequence_recursion(idx+1 , curr + s[idx], s , res)

    subsequence_recursion(idx + 1, curr , s , res)


def all_subsequence_recursion(s):

    res =[]

    subsequence_recursion(0, "", s , res)
    return res 

s = "abc"
print(all_subsequence_recursion(s))