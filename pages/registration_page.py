from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = self.page.get_by_test_id("registration-page-registration-button")
        self.login_link = self.page.get_by_test_id("registration-page-login-link")
        self.user_already_exists_alert = self.page.get_by_test_id("registration-page-user-already-exists-alert")

    def click_registration_button(self) -> None:
        self.registration_button.click()

    def click_login_link(self) -> None:
        self.login_link.click()

    def check_visible_user_already_exists_alert(self) -> None:
        expect(self.user_already_exists_alert).to_be_visible()
        expect(self.user_already_exists_alert).to_have_text("User already exists")
