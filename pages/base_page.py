from re import Pattern

import allure
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str) -> None:
        with allure.step(f"Opening the: {url}"):
            self.page.goto(url)

    def reload(self) -> None:
        with allure.step(f"Reloading page with url: {self.page.url}"):
            self.page.reload()

    def check_current_url(self, expected_url: str | Pattern[str]) -> None:
        with allure.step(f"Checking that current url matches pattern: {expected_url.pattern}"):  # type: ignore[union-attr]
            expect(self.page).to_have_url(expected_url)
