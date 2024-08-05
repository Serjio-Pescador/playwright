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
        self.reset = Button(self._page, locator="//*[@data-testid='menu-btn-files-reset']", name='Reset')
        # self.upload = UploadFiles.set_files(self._page.set_input_files(selector="Upload file", files="./files/AC20-FZK-Haus.ifc"))
        # UploadFiles.set_files(self._page.set_input_files(selector="Upload file", files="./files/AC20-FZK-Haus.ifc"))

    def files_expand(self,):
        self.files.click()

    def local_upload(self,):
        self.files_expand()
        self.local.click()
        self.ifc_upload()



