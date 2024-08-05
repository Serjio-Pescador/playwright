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


    def close_page(self):
        self._page.close()

    def assert_url_window_eql(self, url: str, index_window: int = 0):
        with allure.step(f"Совпадение url страниц на вкладке {index_window}"):
            pages = self._page.context.pages
            expect(pages[index_window]).to_have_url(url)
