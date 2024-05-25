class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #magic method to turn object into a string
    # def __str__(self):
    #     return f"Person {self.name}, {self.age} years old"
    
    #magic method to return a string 
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

bob = Person("Bob", 35)
print(bob)