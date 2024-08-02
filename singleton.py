from playwright.sync_api import sync_playwright, Page


class BaseUrlSingleton:
    _instance = None
    base_url = ""

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def set_base_url(cls, url):
        cls.get_instance().base_url = url

    @classmethod
    def get_base_url(cls):
        url = cls.get_instance().base_url
        return url



class PlaywrightSingleton:
    _instance = None
    _browser = None
    _page = None
    _playwright = None
    _cookies_cache = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def initialize_browser(cls, browser_name="chromium", headless=False, width=1920, height=1080):
        if cls._browser is None:
            cls._playwright = sync_playwright().start()
            browser = getattr(cls._playwright, browser_name)
            cls._browser = browser.launch(headless=headless)
            cls._page = cls._browser.new_page(viewport={'width': width, 'height': height})

    @classmethod
    def get_page(cls) -> Page:
        if cls._page is None:
            raise Exception("Browser not initialized, call initialize_browser first.")
        return cls._page

    @classmethod
    def save_cookies(cls, user_id: int):
        cookies = cls._page.context.cookies()
        cls._cookies_cache[user_id] = cookies

    @classmethod
    def load_cookies(cls, user_id: int) -> bool:
        if user_id in cls._cookies_cache:
            cls._page.context.add_cookies(cls._cookies_cache[user_id])
            return True
        return False

    @classmethod
    def close_browser(cls):
        if cls._page:
            cls._page.close()
            cls._page = None
        if cls._browser:
            cls._browser.close()
            cls._browser = None
        if cls._playwright:
            cls._playwright.stop()
            cls._playwright = None