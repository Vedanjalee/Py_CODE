def minReversals(s):
    
    if len(s) % 2 != 0:
        return -1
    
    
    stack = []
    
    for char in s:
        if char == '{':
           
            stack.append(char)
        elif char == '}':
           
            if stack and stack[-1] == '{':
                stack.pop()  
            else:
                stack.append(char)  

    opening = 0
    closing = 0
    while stack:
        char = stack.pop()
        if char == '{':
            opening += 1
        else:
            closing += 1
    
    reversals = (opening + 1) // 2 + (closing + 1) // 2
    
    return reversals


print(minReversals("}}}}"))  
print(minReversals("{{{{"))  
print(minReversals("{{}}"))  
print(minReversals("}}}}{")) 