import re
from playwright.sync_api import Page, expect
import pytest


@pytest.fixture()
def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("http://localhost:4200/")

#проверка наличия кнопки Файлы на стартовой странице
def test_btn_files(page: Page):
    print("Есть кнопка файлы")
    filesMenuButton = page.get_by_test_id("menu-btn-files")
    expect(filesMenuButton).to_be_visible
    filesMenuButton.screenshot(animations="disabled", path='./test-results/1.1.filesbutton.png')


#проверка наличия тултипа у кнопки Файлы на стартовой странице
def test_btn_files_tooltip(page: Page):
    print("Есть тултип на кнопке Файлы")
    page.get_by_test_id("menu-btn-files").hover(force=True)
    filesMenuButtonTooltip = page.get_by_role("tooltip", name="файлы")
    expect(filesMenuButtonTooltip).to_be_visible
    filesMenuButtonTooltip.screenshot(animations="disabled", path='./test-results/1.2.filesbuttontooltip.png')


#нажатие кнопки Файлы на раскрывает дополнительное меню кнопок
def test_btn_files_click(page: Page):
    print("Нажатие на кнопку Файлы открывает меню файлов")
    page.get_by_test_id("menu-btn-files").click()
    filesbuttonmenu = page.locator(".ant-collapse-content-box")
    expect(filesbuttonmenu).to_be_visible()
    filesbuttonmenu.screenshot(animations="disabled", path='./test-results/1.3.filesbuttonmenu.png')


#нажатие кнопки Файлы модифицирует кнопку в кнопку назад
def test_back_btn(page: Page):
    print("кнопка Файлы модифицируется в кнопку назад")
    page.get_by_test_id("menu-btn-files").click()
    backButton = page.get_by_test_id("menu-btn-back")
    expect(backButton).to_be_visible()
    backButton.screenshot(animations="disabled", path='./test-results/1.4.backbutton.png')


#проверка наличия тултипа у кнопки Назад
def test_back_btn_tooltip(page: Page):
    print("Нажатие на кнопку Файлы открывает меню файлов")
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
    page.set_input_files('input[type="file"]','./tests/AC20-FZK-Haus.ifc')
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
