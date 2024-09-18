import allure
from abc import abstractmethod, ABC
from singleton import PlaywrightSingleton
from playwright.sync_api import expect, Locator


class PageElement(ABC):
    def __init__(self, locator: str, name: str) -> object:
        self.page = PlaywrightSingleton.get_page()
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

    def to_have_attribute(self, name, value, **kwargs):
        with allure.step(f'Есть атрибут у элемента {self._type_of}: "{self._format_name(**kwargs)}".'):
            expect(self._find_element(**kwargs)).to_have_attribute(name, value)

    def to_be_enabled(self, is_enable=True, **kwargs):
        text_report = 'Акивный' if is_enable else 'Не акивный'
        with allure.step(f'Assert: "{self._type_of}" - "{self._format_name(**kwargs)}" {text_report} на странице.'):
            if is_enable:
                expect(self._find_element(**kwargs)).to_be_enabled()
            else:
                expect(self._find_element(**kwargs)).not_to_be_enabled()

    def count(self, count, **kwargs):
        with allure.step(f'Есть атрибут у элемента {self._type_of}: "{self._format_name(**kwargs)}".'):
            expect(self._find_element(**kwargs)).to_have_count(count)

    def press(self, **kwargs):
        with allure.step(f'Зажать и подвигать {self._type_of}: "{self._format_name(**kwargs)}".'):
            self.page.press(self.locator, **kwargs)