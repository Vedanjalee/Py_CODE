def reverse_string(s):
    stack =[]

    # Pull all har to stack

    for char in s:
        stack.append(char)
        # Pop all char to form the reversed string
    reversed_s =""
    while stack:
        reversed_s += stack.pop()
    return reversed_s        

input_string = "hello"
print("Original string:", input_string)
print("Reversed string:", reverse_string(input_string))