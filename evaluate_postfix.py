import math
def evaluate_postfix(expression: str) -> int:
    stack = []
    tokens = expression.split(' ')

    for token in tokens:
        if token.strip() == '':
            continue
        try:
            stack.append(int(token))
        except ValueError:
            op2 = stack.pop()
            op1 = stack.pop()

            if token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)
            elif token == '*':
                stack.append(op1 * op2)
            elif token == '/':
                stack.append(int(op1 / op2))

    return stack.pop()


postfix_expression = "2 1 + 3 *"
result = evaluate_postfix(postfix_expression)
print(f"The result of '{postfix_expression}' is: {result}")
