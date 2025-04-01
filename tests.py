import pytest

class TestAddNewBook:

    @pytest.mark.parametrize("name", ["Book1", "AnotherBook"])
    def test_add_new_book_positive(self, collector, name):
        initial_count = len(collector.books_genre)
        collector.add_new_book(name)
        assert len(collector.books_genre) == initial_count + 1

    @pytest.mark.parametrize("name", ["", "A" * 41])
    def test_add_new_book_negative(self, collector, name):
        initial_count = len(collector.books_genre)
        collector.add_new_book(name)
        assert len(collector.books_genre) == initial_count

class TestSetBookGenre:

    @pytest.mark.parametrize("name, genre", [("Book1", "Фантастика"), ("Book2", "Ужасы")])
    def test_set_book_genre_positive(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_negative(self, collector):
        collector.add_new_book("Book3")
        collector.set_book_genre("Book3", "Неизвестный жанр")
        assert collector.get_book_genre("Book3") == ''

class TestGetBooksGenre:

    def test_get_books_genre(self, collector):
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Фантастика")
        books_genre = collector.get_books_genre()
        assert books_genre == {"Book1": "Фантастика"}

class TestGetBookGenre:

    def test_get_book_genre_positive(self, collector):
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Фантастика")
        assert collector.get_book_genre("Book1") == "Фантастика"

    def test_get_book_genre_negative(self, collector):
        assert collector.get_book_genre("UnknownBook") is None

class TestGetBooksWithSpecificGenre:

    @pytest.mark.parametrize("genre, expected", [
        ("Фантастика", ["Book1"]),
        ("Ужасы", ["Book2"]),
        ("Неизвестный жанр", [])
    ])
    def test_get_books_with_specific_genre(self, collector, genre, expected):
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Фантастика")
        collector.add_new_book("Book2")
        collector.set_book_genre("Book2", "Ужасы")
        assert collector.get_books_with_specific_genre(genre) == expected

class TestGetBooksForChildren:

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Фантастика")
        collector.add_new_book("Book2")
        collector.set_book_genre("Book2", "Ужасы")
        assert collector.get_books_for_children() == ["Book1"]

class TestAddBookInFavorites:

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Book1")
        collector.add_book_in_favorites("Book1")
        assert "Book1" in collector.get_list_of_favorites_books()

class TestDeleteBookFromFavorites:

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Book1")
        collector.add_book_in_favorites("Book1")
        collector.delete_book_from_favorites("Book1")
        assert "Book1" not in collector.get_list_of_favorites_books()

class TestGetListOfFavoritesBooks:

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Book1")
        collector.add_book_in_favorites("Book1")
        assert collector.get_list_of_favorites_books() == ["Book1"]
