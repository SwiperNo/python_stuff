def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor


def calcule(*values, operator):
    return operator(*values)



result = calcule(20, 4, operator=divide)