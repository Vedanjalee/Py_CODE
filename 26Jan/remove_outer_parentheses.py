def remove_outer_paranthesis(s):
    stack = []
    result =[]

    for i , char in enumerate (s):
        if char == '(':
            if stack:
                result.append(char)
            stack.append(char)

        elif char == ')':
            stack.pop() 

            if stack:
                result.append(char)
    return ''.join(result)                    

s= "(()())(())"
s= "(()())(())(()(()))"
print("original :", s)
print("after removing outer brackets :",remove_outer_paranthesis(s))  # Expected: "()()()"

print("original : ", s)
print("after removing outer brackets : ", remove_outer_paranthesis(s))  # Expected: "()()()()(())"