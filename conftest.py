import allure
import pytest
from playwright.sync_api import sync_playwright, Page
import os
from singleton import BaseUrlSingleton


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help='Браузер для запуска тестов')
    parser.addoption('--headless', action='store_true', default=None,
                     help='Запуск браузера без окна')
    parser.addoption('--base_url', action='store', default=os.getenv("HOST", "http://localhost:4200/"),
                     help='Выберите хост, для работы тестов')


@pytest.fixture(scope='session')
def chromium_page(base_url) -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=True)
        yield chromium.new_page()
        chromium.close()


@pytest.fixture(scope="session", autouse=True)
def setup_base_url(request):
    base_url = request.config.getoption("--base_url")
    BaseUrlSingleton.set_base_url(base_url)


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("Running test: ")
    # Go to the starting url before each test.
    page.goto(str(base_url))
    yield
    print("Все тесты были запущены")


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