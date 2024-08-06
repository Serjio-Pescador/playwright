from pages.components.base_element import PageElement


class Text(PageElement):

    @property
    def _type_of(self):
        return 'Text'
