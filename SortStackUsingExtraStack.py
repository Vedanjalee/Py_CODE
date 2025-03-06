def sortStackUsingExtraStack(stack):
    extraStack = []
    
    while stack:
        temp = stack.pop()
        while extraStack and extraStack[-1] > temp:
            stack.append(extraStack.pop())
        extraStack.append(temp)
    
    while extraStack:
        stack.append(extraStack.pop())
    
    return stack

stack = [3, 5, 1, 4, 2]
print(sortStackUsingExtraStack(stack))  # Output: [1, 2, 3, 4, 5]
