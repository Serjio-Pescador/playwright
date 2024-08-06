from pages.components.tooltip import Tooltip
from pages.components.button import Button
from pages.base_page import BasePage


class ViewerPage(BasePage):

    def open_page(self, route=''):
        super().open_page(route)

    def __init__(self, page):
        super().__init__(page)

        self.files = Button(self._page, locator="//*[@data-testid='menu-btn-files']", name='Files')
        self.files_tt = Tooltip(self._page, locator="//*[contains(text(),'файлы')]", name='ТТ файлы')
        self.local = Button(self._page, locator="//*[@data-testid='menu-btn-files-local']", name='Local')
        self.local_tt = Tooltip(self._page, locator="//*[contains(text(),'локально')]", name='ТТ локально')
        self.back = Button(self._page, locator="//*[@data-testid='menu-btn-back']", name='Back')
        self.back_tt = Tooltip(self._page, locator="//*[contains(text(),'назад')]", name='ТТ назад')
        self.demo = Button(self._page, locator="//*[@data-testid='menu-btn-files-demo']", name='Demo')
        self.demo_tt = Tooltip(self._page, locator="//*[contains(text(),'демо')]", name='ТТ демо')
        self.reset = Button(self._page, locator="//*[@data-testid='menu-btn-files-reset']", name='Reset')
        self.reset_tt = Tooltip(self._page, locator="//*[contains(text(),'Сбросить модель')]", name='ТТ Сбросить')

    def files_expand(self,):
        self.files.click()

    def local_upload(self,):
        self.files_expand()
        self.local.click()
        self.ifc_upload()



