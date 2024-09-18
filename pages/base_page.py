import datetime
import allure
from singleton import BaseUrlSingleton, PlaywrightSingleton
from playwright.sync_api import Page, expect
import os
from PIL import Image
from io import BytesIO

def requests_on_page(self, ):
    self._page.on("request", lambda request: print(">>", request.method, request.url))
    self._page.on("response", lambda response: print("<<", response.status, response.url))

class BasePage:
    def __init__(self):
        self._page = PlaywrightSingleton.get_page()
        self.base_url = BaseUrlSingleton.get_base_url()

    def get_page_url(self):
        return self._page.url

    def ifc_full_upload(self, arr):
        self._page.set_input_files('input[type="file"]', files=arr)

    def make_screenshot(self, **kwargs):
        current_date = datetime.datetime.now()
        current_date_string = current_date.strftime('%d%m%y_%H%M%S')
        # self._page.screenshot(animations="disabled", path=f'./screenshots/screenshot_{current_date_string}.png')
        return self._page.screenshot(animations="disabled", **kwargs)


    def test_screenshot(self, image_snapshot, timeout: float = 4000, diff: float = 0.7, **kwargs):
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        screenshot = Image.open(BytesIO(self._page.screenshot(animations="disabled", timeout=timeout, **kwargs)))
        image_snapshot(screenshot, f"./screenshots/{test_name}.png", diff)
        return


    def file_download(self, locator):
        with self._page.expect_download() as download_info:
            locator.click()
        download = download_info.value
        download.save_as("./artifacts/" + download.suggested_filename)

    def close_page(self):
        self._page.close()

    def assert_url_window_eql(self, url: str, index_window: int = 0):
        with allure.step(f"Совпадение url страниц на вкладке {index_window}"):
            pages = self._page.context.pages
            expect(pages[index_window]).to_have_url(url)

    def wait_request(self, ):
        with self._page.expect_event("requestfinished") as request_info:
            requests_on_page(self)
            pass
        request = request_info.value
        print(request.timing)


    def download_type(self, file_type):
        if file_type == 'csv':
            return self.file_download(self.room_checklist_download_btn_csv)
        elif file_type == 'pdf':
            return self.file_download(self.room_checklist_download_btn_pdf)
        elif file_type == 'all':
            return self.file_download(self.room_checklist_download_btn_all)

    def mouse_dblclick(self, x: float, y: float, button: str):
        self._page.mouse.dblclick(x=x, y=y, button=button)