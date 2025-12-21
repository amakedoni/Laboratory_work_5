from custom_collections.book_collection import BookCollection
from custom_collections.index_dict import IndexDict
from models.book import Book
from typing import List, Optional

class Library:
    def __init__(self):
        self.books = BookCollection()
        self.index = IndexDict()

    def add_book(self, book: Book) -> None:
        self.books.add(book)
        self.index.add(book)

    def remove_book(self, isbn_or_book: str | Book) -> Book:
        book = self.books.remove(isbn_or_book)
        self.index.remove(book)
        return book

    def find_by_author(self, author: str) -> List[Book]:
        return self.index.get_by_author(author)

    def find_by_year(self, year: int) -> List[Book]:
        return self.index.get_by_year(year)

    def find_by_isbn(self, isbn: str) -> Optional[Book]:
        return self.index.get_by_isbn(isbn)

    def has_book(self, isbn_or_book: str | Book) -> bool:
        return isbn_or_book in self.index

    def __repr__(self) -> str:
        return f"Library({len(self.books)} books)"