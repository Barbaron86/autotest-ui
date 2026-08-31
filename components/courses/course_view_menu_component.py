from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = self.page.get_by_test_id("course-view-menu-button")
        self.edit_menu_button = self.page.get_by_test_id("course-view-edit-menu-button")
        self.delete_menu_button = self.page.get_by_test_id("course-view-delete-menu-button")

    def click_edit(self, index: int) -> None:
        self.menu_button.nth(int(index)).click()

        expect(self.edit_menu_button.nth(int(index))).to_be_visible()
        self.edit_menu_button.nth(int(index)).click()

    def click_delete(self, index: int) -> None:
        self.menu_button.nth(int(index)).click()

        expect(self.delete_menu_button.nth(int(index))).to_be_visible()
        self.delete_menu_button.nth(int(index)).click()
