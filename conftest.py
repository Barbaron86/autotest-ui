from pytest import Config

from tools.logger import configure_logging

pytest_plugins = ("fixtures.pages", "fixtures.browsers", "tools.allure.logs", "fixtures.allure")


def pytest_configure(config: Config) -> None:
    configure_logging()
