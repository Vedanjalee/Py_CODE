def matching_paranthesis(s):

    stack = [] 

    for char in s :
        if char == '(':
            stack.append(char)

        elif char == ')':
            if not stack :
                return False
            stack.pop()
    return len(stack) == 0     

str1 =   "(a + (b - c) * (d / e))"

str2 = "(a + b) * (c - d))"

str3 = "((a + b)"

print(matching_paranthesis(str1))

print(matching_paranthesis(str2))

print(matching_paranthesis(str3))
                