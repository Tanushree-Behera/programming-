def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

def reverse_stack(stack):
    if not stack:
        return
    top_element = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top_element)

if __name__ == "__main__":
    my_stack = [1, 2, 3, 4]
    print(f"Original stack (top to bottom): {my_stack}")
    reverse_stack(my_stack)
    print(f"Reversed stack (top to bottom): {my_stack}")
