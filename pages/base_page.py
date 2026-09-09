from re import Pattern

import allure
from loguru import logger
from playwright.sync_api import Page, expect

logger = logger.bind(component="BASE_PAGE")


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str) -> None:
        step = f"Opening the: {url}"

        with allure.step(step):
            logger.info(step)
            self.page.goto(url)

    def reload(self) -> None:
        step = f"Reloading page with url: {self.page.url}"

        with allure.step(step):
            logger.info(step)
            self.page.reload()

    def check_current_url(self, expected_url: Pattern[str]) -> None:
        step = f"Checking that current url matches pattern: {expected_url.pattern}"

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
