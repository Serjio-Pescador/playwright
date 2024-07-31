from pages.components.base_element import PageElement


class Image(PageElement):
    @property
    def _type_of(self):
        return 'Image'
