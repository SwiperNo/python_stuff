#def named(**args):
#    print(args)



#named(name="Bobd", age=25)

#example two

#def named(name, age):
 #   print(name, age)

#details = {"name": "Bob", "age": 25}

#named(**details)


#example three
def named(**args):
    print(args)

def print_nicely(**args):
    named(**args)
    for arg, value in args.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)

def both(*args, **kargs)
    print(args)
    print(kargs)

both(1, 3, 5, name="Bob", age=25)
