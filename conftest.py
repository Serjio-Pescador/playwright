import allure
import pytest
import os
from playwright.sync_api import Page

from pages.viewer_page import ViewerPage
from singleton import BaseUrlSingleton, PlaywrightSingleton
from del_checklist import clean_room_checklists
from dotenv import load_dotenv

load_dotenv()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chromium",
                     help='Браузер для запуска тестов')
    parser.addoption('--headless', action='store_true', default=False,
                     help='Запуск браузера без окна')
    parser.addoption('--base_url', action='store', default=os.getenv("HOST", 'http://localhost:4200/'),
                     help='Выберите хост, для работы тестов')


# @pytest.fixture(scope="session")
# def base_url(request):
#     return request.config.getoption("--base_url")


@pytest.fixture(scope="session", autouse=True)
def setup_base_url(request):
    base_url = request.config.getoption("--base_url") or os.getenv("HOST", 'http://localhost:4200/')

    BaseUrlSingleton.set_base_url(base_url)
    return

@pytest.fixture(scope='session')
def browser(request) -> Page:
    browser_name = request.config.getoption('--browser_name')
    headless = request.config.getoption('--headless')

    PlaywrightSingleton.initialize_browser(browser_name, headless)
    page = PlaywrightSingleton.get_page()
    yield page
    PlaywrightSingleton.close_browser()


@pytest.fixture(scope="function")
def viewer_page(browser):
    url = BaseUrlSingleton.get_base_url()
    browser.goto(url, wait_until='domcontentloaded')
    return ViewerPage()


@pytest.fixture(scope="function")
def viewer_delete_checklist():
    clean_room_checklists()
    return


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("chromium_page")
        if page:
            try:
                screenshot = page.screenshot(full_page=True)
                allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(f"Не удалось сделать скриншот: {e}")


