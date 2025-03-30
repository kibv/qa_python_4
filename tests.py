import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()

@pytest.mark.parametrize("name, expected", [
    ("Book1", True),
    ("", False),
    ("A" * 41, False),
    ("Book2", True)
])
def test_add_new_book(collector, name, expected):
    initial_count = len(collector.books_genre)
    collector.add_new_book(name)
    assert (len(collector.books_genre) == initial_count + 1) == expected

def test_add_new_book_existing_name(collector):
    collector.add_new_book("Book1")
    initial_count = len(collector.books_genre)
    collector.add_new_book("Book1")
    assert len(collector.books_genre) == initial_count

@pytest.mark.parametrize("name, genre, expected", [
    ("Book1", "Фантастика", "Фантастика"),
    ("Book2", "Ужасы", "Ужасы"),
    ("Book3", "Неизвестный жанр", '')  # Ожидаем, что жанр останется пустой строкой
])
def test_set_book_genre(collector, name, genre, expected):
    collector.add_new_book(name)
    collector.set_book_genre(name, genre)
    assert collector.get_book_genre(name) == expected

def test_get_book_genre(collector):
    collector.add_new_book("Book1")
    collector.set_book_genre("Book1", "Фантастика")
    assert collector.get_book_genre("Book1") == "Фантастика"
    assert collector.get_book_genre("UnknownBook") is None

@pytest.mark.parametrize("genre, expected", [
    ("Фантастика", ["Book1"]),
    ("Ужасы", ["Book2"]),
    ("Неизвестный жанр", [])
])
def test_get_books_with_specific_genre(collector, genre, expected):
    collector.add_new_book("Book1")
    collector.set_book_genre("Book1", "Фантастика")
    collector.add_new_book("Book2")
    collector.set_book_genre("Book2", "Ужасы")
    assert collector.get_books_with_specific_genre(genre) == expected

def test_get_books_for_children(collector):
    collector.add_new_book("Book1")
    collector.set_book_genre("Book1", "Фантастика")
    collector.add_new_book("Book2")
    collector.set_book_genre("Book2", "Ужасы")
    assert collector.get_books_for_children() == ["Book1"]

def test_add_book_in_favorites(collector):
    collector.add_new_book("Book1")
    collector.add_book_in_favorites("Book1")
    assert "Book1" in collector.get_list_of_favorites_books()

def test_delete_book_from_favorites(collector):
    collector.add_new_book("Book1")
    collector.add_book_in_favorites("Book1")
    collector.delete_book_from_favorites("Book1")
    assert "Book1" not in collector.get_list_of_favorites_books()

def test_get_list_of_favorites_books(collector):
    collector.add_new_book("Book1")
    collector.add_book_in_favorites("Book1")
    assert collector.get_list_of_favorites_books() == ["Book1"]
