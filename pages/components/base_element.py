import allure
from playwright.async_api import Page

from abc import abstractmethod, ABC

from playwright.sync_api import expect, Locator


class PageElement(ABC):
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    @abstractmethod
    def _type_of(self) -> str:
        return 'component'

    def _format_locator(self, **kwargs):
        return self.locator.format(**kwargs)

    def _format_name(self, **kwargs):
        return self.name.format(**kwargs)

    def _find_element(self, **kwargs) -> Locator:
        locator = self._format_locator(**kwargs)
        return self.page.locator(locator)

    def get_text(self, **kwargs) -> str:
        return self._find_element(**kwargs).text_content()

    def click(self, **kwargs):
        with allure.step(f'Нажать {self._type_of}: "{self._format_name(**kwargs)}".'):
            self._find_element(**kwargs).click()

    def hover(self, **kwargs):
        with allure.step(f'Навести курсор на {self._type_of}: "{self._format_name(**kwargs)}".'):
            self._find_element(**kwargs).hover()

    def assert_visibility(self, is_visible=True, **kwargs):
        text_report = 'Отображается' if is_visible else 'Не отображается'
        with allure.step(f'Assert: "{self._type_of}" - "{self._format_name(**kwargs)}" {text_report} на странице.'):
            if is_visible:
                expect(self._find_element(**kwargs)).to_be_visible()
            else:
                expect(self._find_element(**kwargs)).not_to_be_visible()

    def assert_text_eql(self, text, **kwargs):
        with allure.step(f'Assert: "{self._type_of}" - "{self._format_name(**kwargs)}" {text} на странице.'):
            expect(self._find_element(**kwargs)).to_have_text(text)
# Можно сделать отдельно работу с таблицами? модальными окнами
