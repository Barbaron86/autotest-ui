from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.text import Text


class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.delete_exercise_button = Button(
            page, "create-course-exercise-{index}-box-toolbar-delete-exercise-button", "Delete exercise"
        )
        self.subtitle = Text(page, "create-course-exercise-{index}-box-toolbar-subtitle-text", "Exercise subtitle")
        self.title_input = Input(page, "create-course-exercise-form-title-{index}-input", "Title")
        self.description_input = Input(page, "create-course-exercise-form-description-{index}-input", "Description")

    def click_delete_button(self, index: int) -> None:
        self.delete_exercise_button.click(index=index)

    def check_visible(self, index: int, title: str, description: str) -> None:
        self.subtitle.check_visible(index=index)
        self.subtitle.check_have_text(text="#{index + 1} Exercise", index=index)

        self.title_input.check_visible(index=index)
        self.title_input.check_have_value(value=title, index=index)

        self.description_input.check_visible(index=index)
        self.description_input.check_have_value(value=description, index=index)

    def fill_create_exercise_form(self, index: int, title: str, description: str) -> None:
        self.title_input.fill(value=title, index=index)
        self.title_input.check_have_value(value=title, index=index)

        self.description_input.fill(value=description, index=index)
        self.description_input.check_have_value(value=description, index=index)
