import allure
from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement


class Textarea(BaseElement):
    @property
    def type_off(self) -> str:
        return "textarea"

    def get_locator(self, nth: int = 0, **kwargs: str | int) -> Locator:
        return super().get_locator(nth, **kwargs).locator("textarea").first

    def fill(self, value: str, nth: int = 0, **kwargs: str | int) -> None:
        with allure.step(f'Filling {self.type_off} "{self.name}" with value: "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs: str | int) -> None:
        with allure.step(f'Checking that {self.type_off} "{self.name}" has value: "{value}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)
