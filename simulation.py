import random
from models.book import Book, EBook, Audiobook
from models.library import Library
from datetime import datetime

# БАГ №5: глобальная переменная - состояние сохраняется между вызовами
index_rebuilt = False  # <- Не сбрасывается при повторном запуске

def generate_random_book() -> Book:
    titles = ["Молчаливое эхо", "Волны времени", "Багровый горизонт", "Пепел и свет", "Стеклянный лабиринт"]
    authors = ["А. Кларк", "У. Ле Гуин", "Н.К. Джемисин", "Ц. Лю", "Т. Обрехт"]
    genres = ["Фантастика", "Фэнтези", "Антиутопия", "Литературная проза", "Исторический роман"]
    year = random.randint(1950, 2025)
    isbn = f"ISBN-{random.randint(1000000, 9999999)}"

    book_type = random.choice([Book, EBook, Audiobook])

    if book_type == EBook:
        fmt = random.choice(["PDF", "EPUB", "MOBI"])
        return EBook(
            title=random.choice(titles),
            author=random.choice(authors),
            year=year,
            genre=random.choice(genres),
            isbn=isbn,
            file_format=fmt
        )
    elif book_type == Audiobook:
        narrators = ["Морган Фримен", "Нил Гейман", "Майя Энджелоу", "Стивен Фрай"]
        return Audiobook(
            title=random.choice(titles),
            author=random.choice(authors),
            year=year,
            genre=random.choice(genres),
            isbn=isbn,
            narrator=random.choice(narrators)
        )
    else:
        return Book(
            title=random.choice(titles),
            author=random.choice(authors),
            year=year,
            genre=random.choice(genres),
            isbn=isbn
        )

EVENTS = [
    "добавить_книгу",
    "удалить_случайную_книгу",
    "поиск_по_автору",
    "поиск_по_году",
    "поиск_несуществующей_isbn",
    "обновить_индекс",
]

def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    global index_rebuilt  

    if seed is not None:
        random.seed(seed)
        print(f"Симуляция запущена с seed={seed}")
    else:
        print(f"Симуляция запущена (случайный seed)")

    library = Library()
    step = 0

    while step < steps:
        step += 1
        event = random.choice(EVENTS)
        print(f"\n[ШАГ {step:2d}] Событие: {event}")

        try:
            if event == "добавить_книгу":
                book = generate_random_book()
                library.add_book(book)
                print(f"Добавлена: {book}")

            elif event == "удалить_случайную_книгу":
                if len(library.books) == 0:
                    print("Нет книг для удаления")
                    continue
                idx = random.randint(0, len(library.books) - 1)
                book_to_remove = library.books[idx]
                library.remove_book(book_to_remove.isbn)
                print(f"Удалена: {book_to_remove}")

            elif event == "поиск_по_автору":
                if len(library.books) == 0:
                    print("Поиск по автору: библиотека пуста")
                    continue
                authors = list({b.author for b in library.books})
                author = random.choice(authors)
                results = library.find_by_author(author)
                print(f"Найдено {len(results)} книг(и) автора '{author}':")
                for b in results:
                    print(f"   - {b}")

            elif event == "поиск_по_году":
                if len(library.books) == 0:
                    print("Поиск по году: библиотека пуста")
                    continue
                years = list({b.year for b in library.books})
                year = random.choice(years)
                results = library.find_by_year(year)
                print(f"Найдено {len(results)} книг(и) {year} года:")
                for b in results:
                    print(f"   - {b}")

            elif event == "поиск_несуществующей_isbn":
                fake_isbn = f"ISBN-FAKE-{random.randint(1000, 9999)}"
                result = library.find_by_isbn(fake_isbn)
                if result is None:
                    print(f"Книга с ISBN {fake_isbn} не найдена (как и ожидалось)")
                else:
                    print(f"НЕОЖИДАННО! Найдена несуществующая ISBN: {result}")

            elif event == "обновить_индекс":
                # БАГ №4: бессмысленное сравнение через `is`
                dummy_isbn = "dummy"
                if dummy_isbn is library.index._by_isbn:  # <- str is dict -> всегда False
                    print("(баг: условие с is сработало)")

                #БАГ №5: проверка глобального флага
                if index_rebuilt:
                    print("⏭️  Индекс уже перестраивался (глобальный флаг!) — ПРОПУСК")
                    continue

                new_index = IndexDict()
                for book in library.books:
                    new_index.add(book)
                library.index = new_index
                index_rebuilt = True  # <- устанавливаем, но никогда не сбрасываем
                print(f"Индекс перестроен. Теперь содержит {len(library.index)} записей")

        except Exception as e:
            print(f"ОШИБКА: {type(e).__name__}: {e}")

    print(f"\nСимуляция завершена. Итоговое состояние: {library}")