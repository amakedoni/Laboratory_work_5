from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class Book:
    title: str
    author: str
    year: int
    genre: str
    isbn: str

    def __repr__(self) -> str:
        return f"Book('{self.title}' by {self.author}, {self.year}, ISBN: {self.isbn})"

    def __hash__(self) -> int:
        return hash(self.isbn)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn


class EBook(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, file_format: str = "PDF"):
        object.__setattr__(self, 'title', title)
        object.__setattr__(self, 'author', author)
        object.__setattr__(self, 'year', year)
        object.__setattr__(self, 'genre', genre)
        object.__setattr__(self, 'isbn', isbn)
        object.__setattr__(self, 'file_format', file_format)

    def __repr__(self) -> str:
        return f"EBook('{self.title}' by {self.author}, {self.year}, {self.file_format}, ISBN: {self.isbn})"


class Audiobook(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, narrator: str = "Unknown"):
        object.__setattr__(self, 'title', title)
        object.__setattr__(self, 'author', author)
        object.__setattr__(self, 'year', year)
        object.__setattr__(self, 'genre', genre)
        object.__setattr__(self, 'isbn', isbn)
        object.__setattr__(self, 'narrator', narrator)

    def __repr__(self) -> str:
        return f"Audiobook('{self.title}' narrated by {self.narrator}, ISBN: {self.isbn})"