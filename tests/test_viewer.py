import allure
import pytest
from singleton import BaseUrlSingleton



@pytest.mark.regress
class TestUi:

    @allure.story('Viewer')
    @allure.title('Check page URL')
    def test_valid_url(self, viewer_page):
        # Arrange
        expected_url = BaseUrlSingleton.get_base_url()
        # Act
        viewer_page.open_page()
        # Assert
        viewer_page.assert_url_window_eql(expected_url)

    @allure.story('Viewer')
    @allure.title('Check Files button')
    def test_files_btn(self, viewer_page):
        # Act
        viewer_page.open_page()
        # Assert
        viewer_page.files.assert_visibility()

    @allure.story('Viewer')
    @allure.title('Check Back button')
    def test_back_btn(self, viewer_page):
        # Act
        viewer_page.open_page()
        viewer_page.files_expand()
        # Assert
        viewer_page.back.assert_visibility()

    @allure.story('Viewer')
    @allure.title('Check Local button')
    def test_local_btn(self, viewer_page):
        # Act
        viewer_page.open_page()
        viewer_page.files_expand()
        # Assert
        viewer_page.local.assert_visibility()

    @allure.story('Viewer')
    @allure.title('Check Demo button')
    def test_demo_btn(self, viewer_page):
        # Act
        viewer_page.open_page()
        viewer_page.files_expand()
        # Assert
        viewer_page.demo.assert_visibility()

    @allure.story('Viewer')
    @allure.title('Upload file')
    def test_open_ifc(self, viewer_page):
        # Act
        viewer_page.open_page()
        viewer_page.local_upload()
        # Assert
        viewer_page.reset.assert_visibility()

    @allure.story('Viewer')
    @allure.title('Check Files button tooltip')
    def test_files_btn_tt(self, viewer_page):
        # Act
        viewer_page.open_page()
        viewer_page.files.hover()
        # Assert
        viewer_page.files_tt.assert_visibility()

    @allure.story('Viewer')
    @allure.title('Check Local button tooltip')
    def test_local_btn_tt(self, viewer_page):
        # Act
        viewer_page.open_page()
        viewer_page.files_expand()
        viewer_page.local.hover()
        # Assert
        viewer_page.local_tt.assert_visibility()

    @allure.story('Viewer')
    @allure.title('Check Demo button tooltip')
    def test_demo_btn_tt(self, viewer_page):
        # Act
        viewer_page.open_page()
        viewer_page.files_expand()
        viewer_page.demo.hover()
        # Assert
        viewer_page.demo_tt.assert_visibility()

    @allure.story('Viewer')
    @allure.title('Check Back button tooltip')
    def test_back_btn_tt(self, viewer_page):
        # Act
        viewer_page.open_page()
        viewer_page.files_expand()
        viewer_page.back.hover()
        # Assert
        viewer_page.back.assert_visibility()

    @allure.story('Viewer')
    @allure.title('Check Reset button tooltip')
    def test_reset_btn_tt(self, viewer_page):
        # Act
        viewer_page.open_page()
        viewer_page.local_upload()
        viewer_page.reset.hover()
        # Assert
        viewer_page.reset_tt.assert_visibility()