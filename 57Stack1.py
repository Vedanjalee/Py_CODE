stack =[]

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)

top_ele = stack.pop()
print(top_ele, "is  pop")

print(stack, "new val in stack")

if stack:
    print("Top element:", stack[-1])  # Output: 20
else:
    print("Stack is empty!")


print("Is stack empty?", len(stack) == 0) 

print("Stack size:", len(stack)) 