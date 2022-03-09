from book import Book
from logs import *

with open("Available_Books.dat", "a") as f:
    pass

with open("Borrowed_Books.dat", "a") as f1:
    pass


class Library:
    def __init__(self):
        self.name = None
        self.address = None
        self.available_books = []
        self.borrowed_books = []
        self.no_of_books = None

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def refresh(self):
        self.available_books = read_data("Available_books")
        self.borrowed_books = read_data("Borrowed_books")

    def add_book(self):
        book = input("Name of the Book : ")
        author = input("Author Name : ")
        publish_date = input("Publish Date : ")
        no_of_pages = input("No of pages : ")

        b = Book(book, author, publish_date, no_of_pages)
        self.available_books.append(b)
        write_data("Available_books", b)

    def borrow_book(self, person):
        self.available_books = read_data("Available_Books")
        self.borrowed_books = read_data("Borrowed_Books")
        book = input("Name of the book : ")

        for book_ in self.available_books:
            if book_.get_title().lower() == book.lower():
                self.borrowed_books.append(book_)
                self.available_books.remove(book_)
                remove_book("Available_Books", book_)
                write_data("Borrowed_Books", book_)
                person.add_book(book_)
                print("You have successfully borrowed the book!")
                break
        else:
            print("Book is unavailable in the Library!")

    def return_book(self):
        self.refresh()
        my_book = input("Enter the book you want to return : ")
        for books in self.available_books:
            if books.get_title().lower() == my_book:
                self.available_books.append(books)
                self.borrowed_books.remove(books)
                remove_book("Borrowed_books", books)
                write_data("Available_books", books)
                print("You have successfully returned the book")

        else:
            print("Something is wrong")
            self.refresh()
