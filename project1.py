def reverse_stack(stack):
    # Base case: if the stack is empty, return
    if not stack:
        return
    
    # Pop the top element
    top = stack.pop()
    
    # Reverse the remaining stack
    reverse_stack(stack)
    
    # Insert the popped element at the bottom of the reversed stack
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    # Base case: if the stack is empty, push the item
    if not stack:
        stack.append(item)
        return
    
    # Pop the top element
    top = stack.pop()
    
    # Recur for the rest of the stack
    insert_at_bottom(stack, item)
    
    # Push the top element back
    stack.append(top)


stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)  