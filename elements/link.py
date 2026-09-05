from elements.base_element import BaseElement


class Link(BaseElement):
    @property
    def type_off(self) -> str:
        return "link"
