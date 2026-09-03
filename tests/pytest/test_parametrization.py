import pytest
from pytest import FixtureRequest


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0, f"Number {number} is not positive"


@pytest.mark.parametrize("numbers, expected", [(1, 1), (2, 4), (3, 9), (-1, 1)])
def test_several_numbers(numbers: int, expected: int):
    assert numbers**2 == expected


@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])
@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
def test_multiplication_of_numbers(os: str, browser: str):
    assert os in ["macos", "windows", "linux", "debian"]


@pytest.fixture(params=["chromium", "webkit", "firefox"])
def browser(request: FixtureRequest):
    return request.param  # type: ignore[unused-ignore]


def test_open_browser(browser: str):
    print(f"Opening browser: {browser}")


@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    @pytest.mark.parametrize("account", ["Credit card", "Debit card"])
    def test_user_with_operations(self, user: str, account: str):
        print(f"Testing user {user} with account {account}")

    def test_user_without_operations(self, user: str):
        print(f"Testing user {user} without operations")


users = {
    "+79123456782": "User with money on bank account",
    "+79123456789": "User without money on bank account",
    "+79123456780": "User with operations on bank account",
}


@pytest.mark.parametrize(
    "phone_number",
    ["+79123456782", "+79123456789", "+79123456780"],
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}",
)
def test_identifiers(phone_number: str): ...
