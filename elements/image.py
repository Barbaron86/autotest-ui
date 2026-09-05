from elements.base_element import BaseElement


class Image(BaseElement):
    @property
    def type_off(self) -> str:
        return "image"
