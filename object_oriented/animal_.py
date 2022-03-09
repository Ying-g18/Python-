
class Animal:
    num_of_animal = 0

    def __init__(self):
        self.species = None
        self.color = None
        self.name = None
        Animal.num_of_animal += 1

    def set_species(self, species):
        self.species = species

    def set_color(self, color):
        self.color = color

    def set_name(self, name):
        self.name = name

    @classmethod
    def get_num_of_animal(cls):
        return cls.num_of_animal

    def get_specie(self):
        return self.species

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    def __str__(self):
        return f"Hi I am {self.name} and I have {self.color} color. I am a {self.species}"


a1 = Animal()
a1.set_species("Tiger")
a1.set_color("Orange")
a1.set_name("Max")

a2 = Animal()
a2.set_species("Cat")
a2.set_color("Gray")
a2.set_name("Oliva")

print(a1)
print(a2)
print(f"Number of animal {Animal.num_of_animal}")










