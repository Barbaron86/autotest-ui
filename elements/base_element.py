from playwright.sync_api import Locator, Page, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    def get_locator(self, **kwargs: str | int) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator)

    def click(self, **kwargs: str | int) -> None:
        locator = self.get_locator(**kwargs)
        locator.click()

    def check_visible(self, **kwargs: str | int) -> None:
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs: str | int) -> None:
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(text)
