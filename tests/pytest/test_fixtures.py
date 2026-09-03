import pytest


@pytest.fixture(autouse=True)
def send_analysis_data():
    print("[AUTOUSE] Отправка данных для анализа перед каждым тестом")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Настройка окружения для всех тестов")


@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создание данные пользователя один раз на тестовый класс")


@pytest.fixture(scope="module")
def db_connection():
    print("[MODULE] Создание подключения к базе данных один раз на модуль тестов")


@pytest.fixture(scope="package")
def api_client():
    print("[PACKAGE] Создание API клиента один раз на пакет тестов")


@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] Открываем браузер перед на каждый тест")


class TestUserFlow:
    def test_user_can_login(self, settings, user, db_connection, api_client, browser): ...

    def test_user_can_create_course(self, settings, user, db_connection, api_client, browser): ...


class TestAccountFlow:
    def test_user_can_update_profile(self, settings, user, db_connection, api_client, browser): ...

    def test_user_can_delete_account(self, settings, user, db_connection, api_client, browser): ...
