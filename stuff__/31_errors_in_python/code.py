def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

grades = []


print("Welcome to average grade program")
try:
    average = divide(sum(grades), len(grades))
    print(f"The avergae grade is {average}")
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")
else:
    print(f"The avergae grade is {average}")
finally:
    print("Thank you!")
