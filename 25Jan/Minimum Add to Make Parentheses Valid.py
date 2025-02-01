def Minimum_Add_to_Make_Parentheses_Valid(s):
    stack = [] 
    r = 0 
    for char in s :
        if char == '(' :
            stack.append(char)
            r += 1

        elif char == ')':
            stack.append(char)
            r -=1 

    return r 

print(Minimum_Add_to_Make_Parentheses_Valid("()((()()"))

