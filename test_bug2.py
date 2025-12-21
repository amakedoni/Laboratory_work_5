from models.book import Book
from models.library import Library

lib = Library()

for i in range(3):
    b = Book(f"Книга {i+1}", "Один Автор", 2020 + i, "Жанр", f"ISBN-{i}")
    lib.add_book(b)

print("Добавлено 3 книги. Удаляем по одной...")
for i in range(3):
    try:
        lib.remove_book(f"ISBN-{i}")
        print(f"ISBN-{i} удалена")
    except Exception as e:
        print(f"ОШИБКА: {type(e).__name__}: {e}")
        break