def minAddToMakeValid(S) :
    stack = 0
    result = 0

    for char in S:
        if char == '(' :
            stack += 1

        else :
            if stack> 0:
                stack -= 1
            else:
                result += 1

    result += stack 
    return result 

print(minAddToMakeValid("())"))
# 1
