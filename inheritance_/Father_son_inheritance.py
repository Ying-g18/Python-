
class Father:
    def __init__(self):
        self.property = "$80000"
        self.name = "Jack"

    def display_property(self):
        print(f"Father's property = {self.property}")


class Son(Father):

    def __init__(self):
        super().__init__()


s = Son()
print(s.name)
s.display_property()

