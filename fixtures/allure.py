from collections.abc import Iterator

import pytest

from tools.allure.environment import create_allure_environment_file


@pytest.fixture(scope="session", autouse=True)
def save_allure_environment_file() -> Iterator[None]:
    yield
    create_allure_environment_file()
