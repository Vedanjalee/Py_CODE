def strSubstring_find(str1, inside_str) :

    if not inside_str: 
        return 0 
    
    str1_len = len(str1)
    inside_str_len = len(inside_str)

    for i in range(str1_len - inside_str_len + 1):

        if str1[i:i + inside_str_len] == inside_str:
            return i

    return -1 

str1 = "sadbutsad"   
inside_str =   "sad"  

print("Output : ", strSubstring_find(str1 , inside_str))


str1 = "leetcode" 
inside_str =   "leeto"

print("Output : ", strSubstring_find(str1 , inside_str))

