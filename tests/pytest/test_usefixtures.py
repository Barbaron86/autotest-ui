import pytest


@pytest.fixture()
def clear_books_database() -> None:
    print("[FIXTURE] Очистка базы данных")


@pytest.fixture()
def fill_books_database() -> None:
    print("[FIXTURE] Заполнение базы данных тестовыми данными")


@pytest.mark.usefixtures("clear_books_database", "fill_books_database")
def test_read_all_books_in_library():
    print("[TEST] Чтение всех книг в библиотеке")


@pytest.mark.usefixtures("clear_books_database", "fill_books_database")
class TestLibrary:
    def test_read_all_books_in_library(self): ...

    def test_delete_book_from_library(self): ...
