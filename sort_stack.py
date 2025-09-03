def insert_sorted(stack, element):
    if not stack or element >= stack[-1]:
        stack.append(element)
        return

    temp = stack.pop()
    insert_sorted(stack, element)
    stack.append(temp)

def sort_stack(stack):
    if not stack:
        return
    temp = stack.pop()
    sort_stack(stack)
    insert_sorted(stack, temp)

if __name__ == "__main__":
    my_stack = [3, 1, 4, 2]
    print(f"Original stack (top is at the end): {my_stack}")
    
    sort_stack(my_stack)
    
    print(f"Sorted stack (ascending, top is at the end): {my_stack}")
