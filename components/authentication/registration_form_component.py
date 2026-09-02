from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, "registration-form-email-input", "Email")
        self.username_input = Input(page, "registration-form-username-input", "Username")
        self.password_input = Input(page, "registration-form-password-input", "Password")

    def fill(self, email: str, username: str, password: str) -> None:
        self.email_input.fill(email)
        self.email_input.check_have_value(value=email)

        self.username_input.fill(username)
        self.username_input.check_have_value(value=username)

        self.password_input.fill(password)
        self.password_input.check_have_value(value=password)

    def check_visible(self) -> None:
        self.email_input.check_visible()

        self.username_input.check_visible()

        self.password_input.check_visible()

    def check_values(self, email: str, username: str, password: str) -> None:
        self.email_input.check_have_value(value=email)
        self.username_input.check_have_value(value=username)
        self.password_input.check_have_value(value=password)
