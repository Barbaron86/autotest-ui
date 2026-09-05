import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):
    @property
    def type_off(self) -> str:
        return "file input"

    def set_input_files(self, file: str, nth: int = 0, **kwargs: str | int) -> None:
        with allure.step(f'Setting input "{file}" for {self.type_off} "{self.name}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)
