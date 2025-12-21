# test_bug3.py
from custom_collections.book_collection import BookCollection
from models.book import Book

c1 = BookCollection()
c2 = BookCollection()

b = Book("X", "A", 2020, "F", "X")

print("До добавления:")
print("len(c1) =", len(c1))
print("len(c2) =", len(c2))
print("id(c1._books) =", id(c1._books))
print("id(c2._books) =", id(c2._books))
print("Одинаковые id?", id(c1._books) == id(c2._books))

c1.add(b)

print("\nПосле добавления в c1:")
print("len(c1) =", len(c1))  # 1
print("len(c2) =", len(c2))  # 1 ← БАГ!