# write a program to rempove character from string . for each asterik(*) found in string . the program should remove onre characterthat immediately preceded the asteik th enumber of character removed should match the total count of asterik present 

def remove_chars_with_asterisks(s):
    stack =[] 

    for char in s :
        if char == '*' :
            if stack:
                stack.pop() 
        else:
            stack.append(char)
    return ''.join(stack)

s =      input("Enter the string: ")
result = remove_chars_with_asterisks(s)
print("Modified string:", result)


