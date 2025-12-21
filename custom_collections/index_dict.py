from typing import Dict, Set, List
from models.book import Book

class IndexDict:
    def __init__(self):
        self._by_isbn: Dict[str, Book] = {}
        self._by_author: Dict[str, Set[Book]] = {}
        self._by_year: Dict[int, Set[Book]] = {}

    def _add_to_index(self, book: Book) -> None:
        self._by_isbn[book.isbn] = book
        self._by_author.setdefault(book.author, set()).add(book)
        self._by_year.setdefault(book.year, set()).add(book)

    def _remove_from_index(self, book: Book) -> None:
        #БАГ №2: изменение коллекции во время итерации
        # Итерация по .values() + модификация множества -> RuntimeError
        for book_set in self._by_author.values():
            if book in book_set:
                book_set.remove(book)  # ← модификация во время итерации
                break

        for book_set in self._by_year.values():
            if book in book_set:
                book_set.remove(book)
                break

        self._by_isbn.pop(book.isbn, None)

    def add(self, book: Book) -> None:
        self._add_to_index(book)

    def remove(self, isbn_or_book: str | Book) -> Book:
        isbn = isbn_or_book if isinstance(isbn_or_book, str) else isbn_or_book.isbn
        book = self._by_isbn.get(isbn)
        if book is None:
            raise KeyError(f"Книга с ISBN {isbn} отсутствует в индексе")
        self._remove_from_index(book)
        return book

    def get_by_isbn(self, isbn: str) -> Book | None:
        return self._by_isbn.get(isbn)

    def get_by_author(self, author: str) -> List[Book]:
        return sorted(self._by_author.get(author, []), key=lambda b: b.title)

    def get_by_year(self, year: int) -> List[Book]:
        return sorted(self._by_year.get(year, []), key=lambda b: b.title)

    def __len__(self) -> int:
        return len(self._by_isbn)

    def __contains__(self, isbn_or_book: str | Book) -> bool:
        isbn = isbn_or_book if isinstance(isbn_or_book, str) else isbn_or_book.isbn
        return isbn in self._by_isbn

    def __repr__(self) -> str:
        return f"IndexDict({len(self)} книг проиндексировано)"