def insert_at_bottom(stack, element):
   
    if len(stack) == 0:
        stack.append(element)
    else:
        
        temp = stack.pop()
        
        insert_at_bottom(stack, element)
        
        stack.append(temp)


def print_stack(stack):
    print("Stack:", stack)


stack = [1, 2, 3, 4]
print("Original Stack:")
print_stack(stack)

insert_at_bottom(stack, 0)  

print("Stack after inserting 0 at the bottom:")
print_stack(stack)