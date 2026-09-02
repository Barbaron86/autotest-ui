from playwright.sync_api import Page

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = Button(page, "registration-page-registration-button", "Registration")
        self.login_link = Link(page, "registration-page-login-link", "Login")
        self.user_already_exists_alert = Text(
            page, "registration-page-user-already-exists-alert", "User already exists"
        )

    def click_registration_button(self) -> None:
        self.registration_button.click()

    def click_login_link(self) -> None:
        self.login_link.click()

    def check_visible_user_already_exists_alert(self) -> None:
        self.user_already_exists_alert.check_visible()
        self.user_already_exists_alert.check_have_text(text="User already exists")
