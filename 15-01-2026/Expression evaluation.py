def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))

    return stack[0]


if __name__ == "__main__":
    expr = input("Enter postfix expression (space separated): ")
    print("Result:", evaluate_postfix(expr))
