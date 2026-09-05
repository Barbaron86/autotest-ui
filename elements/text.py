from elements.base_element import BaseElement


class Text(BaseElement):
    @property
    def type_off(self) -> str:
        return "text"
