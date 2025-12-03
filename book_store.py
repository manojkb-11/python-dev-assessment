class Book:
    CURRENT_YEAR = 2025

    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        return self.CURRENT_YEAR - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"
book1 = Book(
    title="It Ends with Us",
    author="Colleen Hoover",
    isbn="9781501110368",
    publication_year=1965
)

book2 = Book(
    title="Norwegian Wood",
    author="Haruki Murakami",
    isbn="9780375704024 ",
    publication_year=1972
)
print("Book 1 Details --- >")
print(f"Title: {book1.title}")
print(f"Author: {book1.author}")
print(f"Age: {book1.get_age()} years")
print(f"Summary: {book1.get_summary()}")

print("\nBook 2 Details --- >")
print(f"Title: {book2.title}")
print(f"Author: {book2.author}")
print(f"Age: {book2.get_age()} years")
print(f"Summary: {book2.get_summary()}")