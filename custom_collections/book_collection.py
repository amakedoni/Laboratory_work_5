from typing import Union, List, Iterator, overload
from models.book import Book

class BookCollection:
    #БАГ №3: изменяемое значение по умолчани
    def __init__(self, books: List[Book] = []):  # <- пустой список по умолчанию
        self._books: List[Book] = books

    def __len__(self) -> int:
        return len(self._books)

    @overload
    def __getitem__(self, index: int) -> Book: ...
    @overload
    def __getitem__(self, index: slice) -> 'BookCollection': ...
    def __getitem__(self, index: Union[int, slice]):
        if isinstance(index, slice):
            return BookCollection(self._books[index])
        return self._books[index]

    def __iter__(self) -> Iterator[Book]:
        return iter(self._books)

    def add(self, book: Book) -> None:
        if book in self._books:
            raise ValueError(f"Книга с ISBN {book.isbn} уже существует")
        self._books.append(book)

    def remove(self, isbn_or_book: Union[str, Book]) -> Book:
        isbn = isbn_or_book.isbn if isinstance(isbn_or_book, Book) else isbn_or_book
        for i, b in enumerate(self._books):
            if b.isbn == isbn:
                #БАГ №1: ошибка на единицу — pop(i + 1) вместо pop(i)
                return self._books.pop(i + 1)  # <- вызовет IndexError для последней книги
        raise KeyError(f"Книга с ISBN {isbn} не найдена")

    def __repr__(self) -> str:
        return f"BookCollection({len(self)} books)"