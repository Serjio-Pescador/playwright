import allure

from pages.components.base_element import PageElement


class Button(PageElement):

    @property
    def _type_of(self):
        return 'Button'

    def dblclick(self, **kwargs):
        with allure.step(f'Нажать два раза {self._type_of}: "{self._format_name(**kwargs)}".'):
            self.page.dblclick(self.locator)
