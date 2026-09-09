from pathlib import Path

import allure
from loguru import logger

from elements.base_element import BaseElement

logger = logger.bind(component="FILE_INPUT")


class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return "file input"

    def set_input_files(self, file: str | Path, nth: int = 0, **kwargs: str | int) -> None:
        step = f'Setting input "{file}" for {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.set_input_files(file)
