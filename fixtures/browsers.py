import re
from collections.abc import Iterator

import pytest
from playwright.sync_api import Page, Playwright
from pytest import FixtureRequest

from config import settings
from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page
from tools.routes import AppRoute


@pytest.fixture(params=settings.browsers)
def page(request: FixtureRequest, playwright: Playwright) -> Iterator[Page]:
    yield from initialize_playwright_page(
        playwright=playwright, test_name=request.node.name, browser_type=request.param
    )


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill(
        email=settings.test_user.email, username=settings.test_user.username, password=settings.test_user.password
    )
    registration_page.click_registration_button()

    registration_page.check_current_url(re.compile(".*/#/dashboard"))

    context.storage_state(path=settings.browser_state_file)
    context.close()
    browser.close()


@pytest.fixture(params=settings.browsers)
def page_with_state(request: FixtureRequest, initialize_browser_state, playwright: Playwright) -> Iterator[Page]:
    yield from initialize_playwright_page(
        playwright=playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file,
        browser_type=request.param,
    )
