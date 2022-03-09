

class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.contact = None
        self.dob = None
        self.username = None
        self.password = None
        self.book_collection = []

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_contact(self, contact):
        self.contact = contact

    def set_dob(self, dob):
        self.dob = id

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_contact(self):
        return self.contact

    def get_dob(self):
        return self.dob

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def add_book(self, book):
        self.book_collection.append(book)

    def read_book(self):
        book = input("Book you want to read : ").lower()
        for book_ in self.book_collection:
            if book_.get_title() == book:
                book_.read()
                break
        else:
            print("The book is not in your collection!")
