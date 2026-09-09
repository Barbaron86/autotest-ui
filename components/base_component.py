from re import Pattern

import allure
from loguru import logger
from playwright.sync_api import Page, expect

logger = logger.bind(component="BASE_COMPONENT")


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: str | Pattern[str]) -> None:
        pattern = expected_url.pattern if isinstance(expected_url, Pattern) else expected_url
        step = f"Checking that current url matches pattern: {pattern}"

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
