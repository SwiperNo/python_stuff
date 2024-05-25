#instance method needs to the object to call itself

class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod #the class itself
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")
    

ClassTest.static_method()