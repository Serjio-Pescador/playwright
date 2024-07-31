import allure

from pages.components.base_element import PageElement


class Input(PageElement):

    @property
    def _type_of(self):
        return 'Input'

    def fill(self, text, clear_before=False, **kwargs):
        if clear_before:
            self.clear(**kwargs)
        with allure.step(f'Заполнить {self._type_of}: "{self._format_name(**kwargs)}".{text}'):
            self._find_element(**kwargs).fill(value=text)

    def clear(self, **kwargs):
        with allure.step(f'Очистить {self._type_of}: "{self._format_name(**kwargs)}".'):
            self._find_element(**kwargs).clear()
