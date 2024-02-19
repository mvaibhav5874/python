allowed_operators = "+ - * / % == and or "

def safe_eval(expr):

    for char in expr:
        if char not in allowed_operators and not (char.isdigit() or (char in "True" or char in "False")):
            return "Invalid"
    return eval(expr)
while True:
    user_input = input("Enter an expression (e.g., 45 + 98 - 10): ")
    try:
        result = safe_eval(user_input)
        print("The evaluated result is:", result)
    except ValueError as e:
        print(e)