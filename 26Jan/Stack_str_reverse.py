def stack_rev(s):
    
    stack =[] 
    result = ""

    for char in s :
        stack.append(char)

    while stack :
        result += stack.pop() 
   
   
    return result          

s = "hello"
print("Reversed string:", stack_rev(s))
