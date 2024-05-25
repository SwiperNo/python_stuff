def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    
    return total


print(multiply(1,3,5))

#Passing in a tuple needs to be upacked with the *
#Operator created a named argument
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."
    

print(apply(1,3,6,7, operator="*"))