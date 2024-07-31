import json
import allure
from singleton import BaseUrlSingleton
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self._page = page
        self.host = BaseUrlSingleton.get_base_url()

    def open_page(self, route: str = None):
        url = f"{self.host}{route}" if route else self.host
        self._page.goto(url, wait_until='domcontentloaded')

    # def auth(self, user):
    #     with allure.step(f"Добавить куки для пользователя: {user.userName}"):
    #         domain = self.host.split("//")[-1].split('/')[0]
    #
    #         self._page.goto(self.host, wait_until='domcontentloaded')
    #         cookies = [
    #             {'name': 'token', 'value': user.token, 'domain': domain, 'path': '/'},
    #             {'name': 'userID', 'value': user.userId, 'domain': domain, 'path': '/'},
    #             {'name': 'userName', 'value': user.userName, 'domain': domain, 'path': '/'},
    #             {'name': 'expires', 'value': '2025-02-11T16:33:08.160Z', 'domain': domain, 'path': '/'},
    #         ]
    #
    #         for cookie in cookies:
    #             self._page.context.add_cookies([cookie])
    #
    #         return self
    #
    # def mock(self, endpoint, mock_response, status=304, headers=None):
    #     if headers is None:
    #         headers = {"Content-Type": "application/json"}
    #     body = json.dumps(mock_response)
    #     self._page.route(endpoint, lambda route, request: route.fulfill(
    #         status=status,
    #         headers=headers,
    #         body=body
    #     ))

    def close_page(self):
        self._page.close()

    def assert_url_window_eql(self, url: str, index_window: int = 0):
        with allure.step(f"Совпадение url страниц на вкладке {index_window}"):
            pages = self._page.context.pages
            expect(pages[index_window]).to_have_url(url)
