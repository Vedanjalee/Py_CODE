def min_add_to_make_valid(s):

    stack = [] 
    
    for char in  s:
        if char == '(' :
            stack.append(char)

        elif char is ')':
            if stack and stack[-1] == '(':
                stack.pop() 
            else:
                stack.append(char)
    return len(stack)            



print(min_add_to_make_valid("())"))  # 1
print(min_add_to_make_valid("((("))  # 3