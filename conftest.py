import pytest
import allure
from ui_facade import UiFacade
from singleton import BaseUrlSingleton, PlaywrightSingleton

@pytest.fixture(scope="session", autouse=True)
def setup_base_url(request):
    base_url = request.config.getoption("--base_url")
    BaseUrlSingleton.set_base_url(base_url)


# def upload_file(path_to_file: str, api_client):
#     file = Files.get_file_bytes(path_to_file)
#     return api_client.create_image(file)



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chromium",
                     help='Браузер для запуска тестов')
    parser.addoption('--headless', action='store_true', default=False,
                     help='Запуск браузера без окна')
    parser.addoption('--base_url', action='store',
                     default='http://localhost:4200/',
                     help='Выберите хост, для работы тестов')


@pytest.fixture(scope='session', autouse=True)
def browser(request):
    browser_name = request.config.getoption('--browser_name')
    headless = request.config.getoption('--headless')

    PlaywrightSingleton.initialize_browser(browser_name, headless)
    page = PlaywrightSingleton.get_page()

    yield page
    PlaywrightSingleton.close_browser()


@pytest.fixture(scope="function", autouse=True)
def clean_browser_state(request):
    page = None
    if 'browser' in request.fixturenames:
        page = request.getfixturevalue('browser')
        page.context.clear_cookies()

    yield
    if page:
        page.evaluate("localStorage.clear();")


@pytest.fixture(scope='session')
def ui(browser) -> UiFacade:
    return UiFacade()





@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.outcome not in ("passed", "skipped"):
        page = item.funcargs.get("browser")
        if page:
            try:
                screenshot = page.screenshot(full_page=True)
                allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(f"Не удалось сделать скриншот: {e}")