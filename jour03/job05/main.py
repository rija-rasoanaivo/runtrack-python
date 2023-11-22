def calcule(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "%":
        result = num1 % num2
    else:
        result = "Opérateur non valide"
    
    print(f"{num1} {operator} {num2} = {result}")

calcule(4, "+", 1)
calcule(4, "-", 1)
calcule(4, "*", 1)
calcule(4, "/", 1)
calcule(4, "%", 1)
