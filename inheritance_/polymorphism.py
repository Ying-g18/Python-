
class Duck:
    def talk(self):
        print("Quack Quack")


class Cat:
    def talk(self):
        print("Meow Meow")


class Dog:
    def bark(self):
        print("Wok Wok")


def can_talk(obj):
    if hasattr(obj, "bark"):
        obj.bark()

    elif hasattr(obj, "talk"):
        obj.talk()

    else:
        print("Something is wrong")


d = Duck()
can_talk(d)

d = Cat()
can_talk(d)

d = Dog()
can_talk(d)
