
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self):
        print(f"Hello I am {self.name} and I can speak !")
    def walk(self):
        print(f"Hello I am {self.name} and I can walk !")
    def dance(self):
        print(f"Hello I am {self.name} and I can dance ")
    def __str__(self):
        return f"Hi I am {self.name} and I am {self.age} years old "
    def __repr__(self):
        return f"Hi I am {self.name} and I am {self.age} years old "

p1 = Person("Haru", 18, "female")

p1.walk()
p1.dance()
p1.speak()
print(p1)



