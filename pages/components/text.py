from pages.components.base_element import PageElement
import allure

class Text(PageElement):

    @property
    def _type_of(self):
        return 'Text'
