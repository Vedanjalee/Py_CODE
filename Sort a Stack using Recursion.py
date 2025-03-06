def sortedInsert(stack, element):
   
    if not stack or stack[-1] <= element:
        stack.append(element)
    
    else:
        temp = stack.pop()
        sortedInsert(stack, element)
        stack.append(temp)

def sortStack(stack):
 
    if stack:
        temp = stack.pop()
        sortStack(stack)
        sortedInsert(stack, temp)


stack = [3, 5, 1, 4, 2]
sortStack(stack)
print(stack)  

# Output: [1, 2, 3, 4, 5]
