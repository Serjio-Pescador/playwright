from pages.components.button import Button
from pages.components.upload_files import UploadFiles
from pages.components.base_element import PageElement

from pages.main_page.locators import MainFilesLocators as Locators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        self.open_page()
        self.button_files_h = Button(locator=Locators.MAIN_FILES_BTN, name="файлы").hover()
        self.button_files = Button(locator=Locators.MAIN_FILES_BTN, name="Кнопка файлы").click()

        self.button_back_h = Button(locator=Locators.FILES_BACK_BTN, name="Назад").hover()
        self.button_back = Button(locator=Locators.FILES_BACK_BTN, name="кнопка Назад").click()

        self.local_upload_h = Button(locator=Locators.LOCAL_FILES_UPLOAD, name="локально").hover()
        self.local_upload = Button(locator=Locators.LOCAL_FILES_UPLOAD, name="кнопка локально").click()
        self.local_upload_file = UploadFiles.set_files(path='./files/AC20-FZK-Haus.ifc')

        self.demo_h = Button(locator=Locators.DEMO_BTN, name="Демо").hover()
        self.demo = Button(locator=Locators.DEMO_BTN, name="кнопка Демо").click()

