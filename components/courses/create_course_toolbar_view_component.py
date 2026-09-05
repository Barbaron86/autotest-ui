import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "create-course-toolbar-title-text", "Create course title")

        self.create_course_button = Button(page, "create-course-toolbar-create-course-button", "Create course")

    @allure.step("Check visible create course toolbar")
    def check_visible(self, title: str = "Create course", is_create_course_disabled: bool = True) -> None:
        self.title.check_visible()
        self.title.check_have_text(text=title)

        self.create_course_button.check_visible()

        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()

    def click_create_course_button(self) -> None:
        self.create_course_button.click()
