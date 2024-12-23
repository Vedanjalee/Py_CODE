def  is_balanced(s):
    stack =[]
    brackets ={
         ')':'(', 
         '}':'{',
         ']' : '['
        }
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack and stack[-1] == brackets[char] :
                stack.pop()
            else:
                return False
    return not stack                 

expression = "{[()()]}"
print(f"Is the expression '{expression}' balanced? {is_balanced(expression)}")