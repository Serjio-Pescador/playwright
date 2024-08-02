from pages.components.button import Button
from pages.components.upload_files import UploadFiles
from pages.components.base_element import PageElement

from pages.main_page.locators import MainFilesLocators as Locators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self):
        super().__init__()

        self.button_files = Button(locator=Locators.MAIN_FILES_BTN, name="Файлы")
        self.button_back = Button(locator=Locators.FILES_BACK_BTN, name="Назад")
        self.local_upload = Button(locator=Locators.LOCAL_FILES_UPLOAD, name="Локально")
        self.demo = Button(locator=Locators.DEMO_BTN, name="Демо")

