def calculate(action, num1, num2):
    if action not in "+-*/":
        return "WRONG INPUT"

    if action == '+':
        return num1 + num2
    elif action == '-':
        return num1 - num2
    elif action == '*':
        return num1 * num2
    elif action == '/':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
calculate()
