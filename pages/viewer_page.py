from pages.components.input import Input
from pages.components.button import Button
from pages.components.upload_files import UploadFiles
from pages.base_page import BasePage


class ViewerPage(BasePage):

    def open_page(self, route=''):
        super().open_page(route)

    def __init__(self, page):
        super().__init__(page)

        self.files = Button(self._page, locator="//*[@data-testid='menu-btn-files']", name='Files')
        self.local = Button(self._page, locator="//*[@data-testid='menu-btn-files-local']", name='Local')
        self.back = Button(self._page, locator="//*[@data-testid='menu-btn-back']", name='Back')
        self.demo = Button(self._page, locator="//*[@data-testid='menu-btn-files-demo']", name='Demo')
        self.upload = UploadFiles(self._page, locator="./files/AC20-FZK-Haus.ifc", name="file.ifc")


    def files_expand(self,):
            self.files.click()

    def local_upload(self, path):
            self.files.click()
            self.local.click()
            self.upload(path)



