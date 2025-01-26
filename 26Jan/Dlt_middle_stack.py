def delete_middle(stack, current_index=0):
    if not stack:
        return
    
    top = stack.pop()
    
    if current_index == len(stack) // 2:
        return
    
    
    delete_middle(stack, current_index + 1)
    
    stack.append(top)


def print_stack(stack):
    print("Stack:", stack)

stack = [1, 2, 3, 4, 5]
print("Original Stack:")
print_stack(stack)

delete_middle(stack)
print("Stack after deleting the middle element:")
print_stack(stack)
