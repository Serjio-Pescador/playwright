from singleton import BaseUrlSingleton, PlaywrightSingleton
from pages.main_page.main_page import MainPage


class UiFacade:
    viewer_page: 'MainPage'

    def __init__(self):
        self._browser = PlaywrightSingleton.get_page()
        self._base_url = BaseUrlSingleton.get_base_url()
        self._page_instances = {}

    def __getattr__(self, name):
        if name not in self._page_instances:
            self._page_instances[name] = self._initialize_page(name)
        return self._page_instances[name]

    def _initialize_page(self, name):
        page_classes = {
            'viewer_page': MainPage
        }
        if name in page_classes:
            return page_classes[name]()
        else:
            raise AttributeError(f"No such page: {name}")

