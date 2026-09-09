import allure
from loguru import logger
from playwright.sync_api import Locator, Page, expect

logger = logger.bind(component="BASE_ELEMENT")


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def type_of(self) -> str:
        return "base element"

    def get_locator(self, nth: int = 0, **kwargs: str | int) -> Locator:
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with "data-testid: {locator}" at index "{nth}"'

        with allure.step(step):
            logger.debug(step)
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs: str | int) -> None:
        step = f'Clicking on {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs: str | int) -> None:
        step = f'Checking that {self.type_of} "{self.name}" is visible'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs: str | int) -> None:
        step = f'Checking that {self.type_of} "{self.name}" has text: "{text}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)
