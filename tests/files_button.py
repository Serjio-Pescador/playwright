import allure
import pytest
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

# class TestProfile:

@pytest.fixture()
def test_main_page(page: Page):
    expect(page.get_base_url()).to_have_url("http://localhost:4200/")


@allure.title('Тесты кнопки Файлы')
@allure.description('Проверка наличия кнопки Файлы на стартовой странице')
@allure.tag('кнопка Файлы')
def test_btn_files(page: Page):
    filesMenuButton = page.get_by_test_id("menu-btn-files")
    filesMenuButton.screenshot(animations="disabled", path='./test-results/1.1.filesbutton.png')


@allure.title('Тесты кнопки Файлы')
@allure.description('проверка наличия тултипа у кнопки Файлы на стартовой странице')
@allure.tag('кнопка Файлы')
def test_btn_files_tooltip(page: Page):
    page.get_by_test_id("menu-btn-files").hover(force=True)
    filesMenuButtonTooltip = page.get_by_role("tooltip", name="файлы")
    filesMenuButtonTooltip.screenshot(animations="disabled", path='./test-results/1.2.filesbuttontooltip.png')


@allure.title('Тесты кнопки Файлы')
@allure.description('нажатие кнопки Файлы на раскрывает дополнительное меню кнопок')
@allure.tag('кнопка Файлы')
def test_btn_files_click(page: Page):
    page.get_by_test_id("menu-btn-files").click()
    filesbuttonmenu = page.locator(".ant-collapse-content-box")
    expect(filesbuttonmenu).to_be_visible()
    filesbuttonmenu.screenshot(animations="disabled", path='./test-results/1.3.filesbuttonmenu.png')


@allure.title('Тесты кнопки Файлы')
@allure.description('нажатие кнопки Файлы модифицирует кнопку в кнопку назад')
@allure.tag('кнопка Файлы')
def test_back_btn(page: Page):
    page.get_by_test_id("menu-btn-files").click()
    backButton = page.get_by_test_id("menu-btn-back")
    expect(backButton).to_be_visible()
    backButton.screenshot(animations="disabled", path='./test-results/1.4.backbutton.png')


@allure.title('Тесты кнопки Файлы')
@allure.description('проверка наличия тултипа у кнопки Назад')
@allure.tag('кнопка Файлы')
def test_back_btn_tooltip(page: Page):
    page.get_by_test_id("menu-btn-files").click()
    page.get_by_role("button", name="arrow-left").hover(force=True)
    back_btn_tooltip = page.get_by_role("tooltip", name="назад")
    expect(back_btn_tooltip).to_be_visible()
    back_btn_tooltip.screenshot(animations="disabled", path='./test-results/1.5.backbuttontooltip.png')


#нажатие кнопки назад сворачивает меню файлы
def test_back_btn_click(page: Page):
    print("Нажатие на кнопку Файлы сворачивает меню файлов")
    page.get_by_test_id("menu-btn-files").click()
    page.get_by_role("button", name="arrow-left").click()
    expect(page.locator(".ant-collapse-content-box > button").first).to_be_hidden()
    page.screenshot(animations="disabled", path='./test-results/1.6.backbuttonclick.png')


# кнопка локально
def test_btn_local(page: Page):
    print("Есть кнопка Локально")
    page.get_by_test_id("menu-btn-files").click()
    localUploadButton = page.get_by_test_id("menu-btn-files-local")
    expect(localUploadButton).to_be_visible()
    localUploadButton.screenshot(animations="disabled", path='./test-results/1.7.localuploadbutton.png')


# есть тултип у кнопки локально
def test_btn_local_tooltip(page: Page):
    print("есть тултип у кнопки локально")
    page.get_by_test_id("menu-btn-files").click()
    page.get_by_test_id("menu-btn-files-local").hover(force=True)
    localbtntooltip = page.get_by_role("tooltip", name="локально")
    expect(localbtntooltip).to_be_visible()
    localbtntooltip.screenshot(animations="disabled", path='./test-results/1.8.localuploadbuttontooltip.png')


#загрузка файла локально
def test_btn_local_upload(page: Page):
    print("загрузка файла локально")
    page.get_by_test_id("menu-btn-files").click()
    page.get_by_test_id("menu-btn-files-local").click()
    page.set_input_files('input[type="file"]','./files/AC20-FZK-Haus.ifc')
    page.screenshot(animations="disabled", path='./test-results/1.9.localuploadbfile.png')

# кнопка демо
def test_btn_demo(page: Page):
    print("Есть кнопка Локально")
    page.get_by_test_id("menu-btn-files").click()
    localUploadButton = page.get_by_test_id("menu-btn-files-demo")
    expect(localUploadButton).to_be_visible()
    localUploadButton.screenshot(animations="disabled", path='./test-results/1.10.demouploadbutton.png')


# есть тултип у кнопки демо
def test_btn_demo_tooltip(page: Page):
    print("есть тултип у кнопки локально")
    page.get_by_test_id("menu-btn-files").click()
    page.get_by_test_id("menu-btn-files-demo").hover(force=True)
    localbtntooltip = page.get_by_role("tooltip", name="демо")
    expect(localbtntooltip).to_be_visible()
    localbtntooltip.screenshot(animations="disabled", path='./test-results/1.11.demouploadbuttontooltip.png')
