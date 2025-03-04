def smallestSubsequence(s):
    last_occurence = {}
    for idx,char in enumerate(s):
        # below in last_occ it is storing last seen idx of char
        last_occurence[char] = idx   

    stack =[] 
    seen =set() 

    for index, char in enumerate(s):
        if char in seen :
            continue 

        while stack and char<stack[-1] and last_occurence[stack[-1]] > index:
            removed_char = stack.pop()
            seen.remove(removed_char)

        stack.append(char)
        seen.add(char)
    return "".join(stack)    

s = "bcabc"
print(smallestSubsequence(s))

