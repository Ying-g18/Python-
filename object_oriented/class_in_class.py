
class Person:
    def __init__(self):
        self.name = "Haru"
        self.age = "18"

    def __str__(self):
        return f"Hi I am {self.name}. I am {self.age} years old"

    class DOB:
        def __init__(self):
            self.day = 18
            self.month = "June"
            self.year = 2003


p1 = Person()
dob = p1.DOB()
print(dob.month)