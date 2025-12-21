from models.book import Book
from models.library import Library

lib = Library()
b = Book("Тест", "Автор", 2020, "Жанр", "1")
lib.add_book(b)
print("Книга добавлена. Кол-во:", len(lib.books))

print("Попытка удалить...")
lib.remove_book("1") 