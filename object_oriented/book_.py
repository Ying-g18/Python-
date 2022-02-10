
class Book:
    def __init__(self, name, author, page):
        self.name = name
        self.author = author
        self.page = page

    def read(self):
        print(f"{self.name} written by {self.author}")

    def getNumbPage(self):
        print(f"Number of page is {self.page} ")


b1 = Book("Wuthering Heights", "Emily", 167)

b1.read()
b1.getNumbPage()