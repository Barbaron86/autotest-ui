from collections.abc import Iterator

import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture()
def chromium_page(playwright: Playwright) -> Iterator[Page]:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()
