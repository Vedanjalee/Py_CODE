def merge_alternately(word1, word2) :
    result =[] 
    i, j = 0, 0

    len1, len2 = len(word1), len(word2) 
    while i<len1 or j<len2 :
        if i<len1 :
            result.append(word1[i])
            i+= 1

        if j<len2:
            result.append(word2[j]) 
            j += 1 
    return "".join(result)      
word1 = "abc"
word2 = "pqrxyz"
print(merge_alternately(word1, word2))      