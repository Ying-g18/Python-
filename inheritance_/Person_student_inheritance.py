
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I can speak")

    def eat(self):
        print("I can eat")


class Student(Person):
    def __init__(self, name="Julie", age=18):
        super().__init__(name, age)

    def skip_class(self):
        print("I can skip class")

    def __str__(self):
        return f"Hi I am {self.name} and {self.age} years old"


s = Student()
s.eat()
s.speak()
print(s)
