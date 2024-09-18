import allure
import pytest
from singleton import BaseUrlSingleton
from pages.viewer_page import TooltipName
from static.test_data import TestData


@pytest.mark.regress
@allure.epic('UI')
@allure.story('Файлы кнопка и загрузка')
class TestFiles:

    @allure.title('Check page URL')
    def test_valid_url(self, viewer_page):
        # Arrange
        expected_url = BaseUrlSingleton.get_base_url()

        # Assert
        viewer_page.assert_url_window_eql(expected_url)

    @allure.title('Появление назад')
    def test_back_btn(self, viewer_page):
        # Act
        viewer_page.files.click()

        # Assert
        viewer_page.back.assert_visibility()

    @allure.title('Локально')
    def test_local_btn(self, viewer_page):
        # Act
        viewer_page.files.click()

        # Assert
        viewer_page.local.assert_visibility()

    @allure.title('Демо')
    def test_demo_btn(self, viewer_page):
        # Act
        viewer_page.files.click()

        # Assert
        viewer_page.demo.assert_visibility()

    @allure.title('Загрузка файла')
    def test_open_ifc(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_haus)

        # Assert
        viewer_page.reset.assert_visibility()

    @allure.title('файлы')
    def test_files_btn_tt(self, viewer_page):
        # Act
        viewer_page.files.hover()
        tooltip_text = TooltipName.tt_files.value

        # Assert
        viewer_page.tooltip.assert_visibility(tooltip_text=tooltip_text)
        viewer_page.tooltip.assert_text_eql(tooltip_text=tooltip_text, text=tooltip_text)

    @allure.title('локально')
    def test_local_btn_tt(self, viewer_page):
        # Act
        viewer_page.files.click()
        viewer_page.local.hover()
        tooltip_text = TooltipName.tt_local.value

        # Assert
        viewer_page.tooltip.assert_visibility(tooltip_text=tooltip_text)
        viewer_page.tooltip.assert_text_eql(tooltip_text=tooltip_text, text=tooltip_text)

    @allure.title('демо')
    def test_demo_btn_tt(self, viewer_page):
        # Act
        viewer_page.files.click()
        viewer_page.demo.hover()
        tooltip_text = TooltipName.tt_demo.value

        # Assert
        viewer_page.tooltip.assert_visibility(tooltip_text=tooltip_text)
        viewer_page.tooltip.assert_text_eql(tooltip_text=tooltip_text, text=tooltip_text)

    @allure.title('назад')
    def test_back_btn_tt(self, viewer_page):
        # Act
        viewer_page.files.click()
        viewer_page.back.hover()
        tooltip_text = TooltipName.tt_back.value

        # Assert
        viewer_page.tooltip.assert_visibility(tooltip_text=tooltip_text)
        viewer_page.tooltip.assert_text_eql(tooltip_text=tooltip_text, text=tooltip_text)

    @allure.title('сбросить')
    def test_reset_btn_tt(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_haus)
        viewer_page.reset.hover()
        tooltip_text = TooltipName.tt_reset.value

        # Assert
        viewer_page.tooltip.assert_visibility(tooltip_text=tooltip_text)
        viewer_page.tooltip.assert_text_eql(tooltip_text=tooltip_text, text=tooltip_text)