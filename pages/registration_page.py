from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = self.page.get_by_test_id("registration-form-email-input").locator("input")
        self.username_input = self.page.get_by_test_id("registration-form-username-input").locator("input")
        self.password_input = self.page.get_by_test_id("registration-form-password-input").locator("input")
        self.registration_button = self.page.get_by_test_id("registration-page-registration-button")
        self.login_link = self.page.get_by_test_id("registration-page-login-link")
        self.user_already_exists_alert = self.page.get_by_test_id("registration-page-user-already-exists-alert")

    def fill_registration_form(self, email: str, username: str, password: str) -> None:
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_registration_button(self) -> None:
        self.registration_button.click()

    def click_login_link(self) -> None:
        self.login_link.click()

    def check_visible_user_already_exists_alert(self) -> None:
        expect(self.user_already_exists_alert).to_be_visible()
        expect(self.user_already_exists_alert).to_have_text("User already exists")
