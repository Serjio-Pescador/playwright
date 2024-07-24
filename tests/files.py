import re
from playwright.sync_api import Page, expect
import pytest
# import asyncio
# from playwright.async_api import async_playwright, Playwright



# async def run(playwright: Playwright):
#     chromium = playwright.chromium # or "firefox" or "webkit".
#     browser = await chromium.launch()
#     page = await browser.new_page()
#     await page.goto("http://localhost:4200/")
#     await browser.close()


# async def main():
#     async with async_playwright() as playwright:
#         await run(playwright)
# asyncio.run(main())


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("Running test: ")
    print("Test is: ${testInfo.status}")
    # Go to the starting url before each test.
    page.goto("http://localhost:4200/")
    yield
    
    print("Все тесты были запущены")



def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("http://localhost:4200/")



#проверка наличия кнопки Файлы на стартовой странице
def test_btn_files(page: Page):
    print("Есть кнопка файлы")
    filesMenuButton = page.locator(".css-dev-only-do-not-override-98ntnt").first
    expect(filesMenuButton).to_be_visible; 
    filesMenuButton.screenshot(animations="disabled", path='./test-results/1.1.filesbutton.png')


#проверка наличия тултипа у кнопки Файлы на стартовой странице
def test_btn_files_tooltip(page: Page):
    print("Есть тултип на кнопке Файлы")
    page.locator(".css-dev-only-do-not-override-98ntnt").first.hover(force=True)
    filesMenuButtonTooltip = page.get_by_role("tooltip", name="файлы")
    expect(filesMenuButtonTooltip).to_be_visible
    filesMenuButtonTooltip.screenshot(animations="disabled", path='./test-results/1.2.filesbuttontooltip.png')


#нажатие кнопки Файлы на раскрывает дополнительное меню кнопок
def test_btn_files_click(page: Page):
    print("Нажатие на кнопку Файлы открывает меню файлов")
    page.locator(".css-dev-only-do-not-override-98ntnt").first.click()
    filesCollapsMenu = page.locator(".ant-collapse-content-box")
    expect(page.locator(".ant-collapse-content-box")).to_be_visible()
    filesCollapsMenu.screenshot(animations="disabled", path='./test-results/1.3.filesbuttonmenu.png')


#нажатие кнопки Файлы модифицирует кнопку в кнопку назад
def test_back_btn(page: Page):
    print("Нажатие на кнопку Файлы открывает меню файлов")
    page.locator(".css-dev-only-do-not-override-98ntnt").first.click()
    backButton = page.get_by_role("button", name="arrow-left")
    expect(backButton).to_be_visible()
    backButton.screenshot(animations="disabled", path='./test-results/1.4.backbutton.png')


#проверка наличия тултипа у кнопки Назад
def test_back_btn_tooltip(page: Page):
    print("Нажатие на кнопку Файлы открывает меню файлов")
    page.locator(".css-dev-only-do-not-override-98ntnt").first.click()
    page.get_by_role("button", name="arrow-left").hover(force=True)
    back_btn_tooltip = page.get_by_role("tooltip", name="назад")
    expect(back_btn_tooltip).to_be_visible()
    back_btn_tooltip.screenshot(animations="disabled", path='./test-results/1.5.backbuttontooltip.png')


#нажатие кнопки назад сворачивает меню файлы
def test_back_btn_click(page: Page):
    print("Нажатие на кнопку Файлы открывает меню файлов")
    page.locator(".css-dev-only-do-not-override-98ntnt").first.click()
    page.get_by_role("button", name="arrow-left").click()
    expect(page.locator(".css-dev-only-do-not-override-98ntnt").first).to_be_visible()
    page.screenshot(animations="disabled", path='./test-results/1.6.backbuttonclick.png')


# кнопка локально
def test_btn_local_click(page: Page):
    print("Нажатие на кнопку Файлы открывает меню файлов")
    page.locator(".css-dev-only-do-not-override-98ntnt").first.click()
    localUploadButton = page.locator(".ant-collapse-content-box > button").first
    expect(localUploadButton).to_be_visible()
    localUploadButton.screenshot(animations="disabled", path='./test-results/1.7.localuploadbutton.png')
    
