import allure
import pytest
from playwright.sync_api import Page, expect
from pages.locators import MainFilesLocators as Locators


@pytest.fixture()
def test_main_page(page: Page):
    expect(page.get_base_url()).to_have_url("http://localhost:4200/")


@allure.title('Тесты Viewer')
@allure.description('Проверка наличия кнопки Файлы на стартовой странице')
@allure.story('кнопка Файлы')
def test_btn_files(page: Page):
    # page.get_by_test_id("menu-btn-files")
    expect(page.locator(Locators.MAIN_FILES_BTN)).to_be_visible()



@allure.title('Тесты Viewer')
@allure.description('проверка наличия тултипа у кнопки Файлы на стартовой странице')
@allure.story('кнопка Файлы')
def test_btn_files_tooltip(page: Page):
    page.locator(Locators.MAIN_FILES_BTN).hover(force=True)
    expect(page.get_by_role("tooltip", name="файлы")).to_be_visible()


@allure.title('Тесты Viewer')
@allure.description('нажатие кнопки Файлы на раскрывает дополнительное меню кнопок')
@allure.story('кнопка Файлы')
def test_btn_files_click(page: Page):
    page.locator(Locators.MAIN_FILES_BTN).click()
    expect(page.locator(Locators.FILES_ALL_TYPES)).to_be_visible()


@allure.title('Тесты Viewer')
@allure.description('нажатие кнопки Файлы модифицирует кнопку в кнопку назад')
@allure.story('кнопка Файлы')
def test_back_btn(page: Page):
    page.locator(Locators.MAIN_FILES_BTN).click()
    expect(page.locator(Locators.FILES_BACK_BTN)).to_be_visible()


@allure.title('Тесты Viewer')
@allure.description('проверка наличия тултипа у кнопки Назад')
@allure.story('кнопка Файлы')
def test_back_btn_tooltip(page: Page):
    page.locator(Locators.MAIN_FILES_BTN).click()
    page.locator(Locators.FILES_BACK_BTN).hover(force=True)
    expect(page.get_by_role("tooltip", name="назад")).to_be_visible()



@allure.title('Тесты Viewer')
@allure.description('нажатие кнопки назад сворачивает меню файлы')
@allure.story('кнопка Файлы')
def test_back_btn_click(page: Page):
    page.locator(Locators.MAIN_FILES_BTN).click()
    page.locator(Locators.FILES_BACK_BTN).click()
    expect(page.locator(Locators.FILES_ALL_TYPES)).to_be_hidden()



@allure.title('Тесты Viewer')
@allure.description('кнопка локально')
@allure.story('кнопка Файлы')
def test_btn_local(page: Page):
    page.locator(Locators.MAIN_FILES_BTN).click()
    expect(page.locator(Locators.LOCAL_FILES_UPLOAD)).to_be_visible()



@allure.title('Тесты Viewer')
@allure.description('есть тултип у кнопки локально')
@allure.story('кнопка Файлы')
def test_btn_local_tooltip(page: Page):
    page.locator(Locators.MAIN_FILES_BTN).click()
    page.locator(Locators.LOCAL_FILES_UPLOAD).hover(force=True)
    expect(page.get_by_role("tooltip", name="локально")).to_be_visible()



@allure.title('Тесты Viewer')
@allure.description('загрузка файла локально')
@allure.story('кнопка Файлы')
def test_btn_local_upload(page: Page):
    page.locator(Locators.MAIN_FILES_BTN).click()
    page.locator(Locators.LOCAL_FILES_UPLOAD).click()
    page.set_input_files('input[type="file"]','./files/AC20-FZK-Haus.ifc')
    page.screenshot(animations="disabled", path='./test-results/1.9.localuploadbfile.png')


@allure.title('Тесты Viewer')
@allure.description('кнопка демо')
@allure.story('кнопка Файлы')
def test_btn_demo(page: Page):
    page.locator(Locators.MAIN_FILES_BTN).click()
    expect(page.locator(Locators.DEMO_BTN)).to_be_visible()


@allure.title('Тесты Viewer')
@allure.description('есть тултип у кнопки демо')
@allure.story('кнопка Файлы')
def test_btn_demo_tooltip(page: Page):
    page.locator(Locators.MAIN_FILES_BTN).click()
    page.locator(Locators.DEMO_BTN).hover(force=True)
    expect(page.get_by_role("tooltip", name="демо")).to_be_visible()
