from re import Pattern

from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str) -> None:
        self.page.goto(url)

    def reload(self) -> None:
        self.page.reload()

    def check_current_url(self, expected_url: str | Pattern[str]) -> None:
        expect(self.page).to_have_url(expected_url)
