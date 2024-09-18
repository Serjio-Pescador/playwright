import allure
import pytest, os
from singleton import BaseUrlSingleton
from pages.viewer_page import TooltipName
from static.test_data import TestData
from conftest import viewer_delete_checklist
from utils.checklists_api import ChecklistsApi
import requests
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

@pytest.mark.regress
@allure.story('ЗАМЕЧАНИЯ')
class TestIssues:

    @allure.title('Check page URL')
    def test_valid_url(self, viewer_page):
        # Arrange
        expected_url = BaseUrlSingleton.get_base_url()

        # Assert
        viewer_page.assert_url_window_eql(expected_url)


    @allure.title('Замечания тултип кнопки')
    def test_issues_btn_tt(self, viewer_page):
        # Act
        viewer_page.issue_btn.hover()
        tooltip_text = TooltipName.tt_issues.value

        # Assert
        viewer_page.tooltip.assert_visibility(tooltip_text=tooltip_text)
        viewer_page.tooltip.assert_text_eql(tooltip_text=tooltip_text, text=tooltip_text)


    @allure.title('Окно списка замечаний')
    def test_list_window_tittle(self, viewer_page):
        # Act
        viewer_page.issue_btn.click()
        title = TooltipName.tt_issues.value

        # Assert
        viewer_page.rooms_list_window_title.assert_text_eql(title=title, text=title)

    @allure.title('Окно списка замечаний')
    def test_list_window_close(self, viewer_page):
        # Act
        viewer_page.issue_btn.click()
        viewer_page.issue_list_close.click()

        # Assert
        viewer_page.rooms_list_window.assert_visibility(is_visible=False)


    @allure.title('Создать замечание')
    def test_create_issue(self, viewer_page):
        # Act
        viewer_page.issue_btn.click()
        viewer_page.issue_add.click()
        viewer_page.issue_add.get_text()
        text_on_button = "Кликните дважды по модели"

        # Assert
        viewer_page.issue_add.assert_text_eql(text_on_button)


    @allure.title('Создать метку замечание')
    def test_create_mark_issue(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_haus)
        viewer_page.issue_btn.click()
        viewer_page.issue_add.click()
        viewer_page.mouse_dblclick(x=700, y=550, button='left')

        # Assert
        viewer_page.issue_details_window.assert_visibility()


    @allure.title('Метка не ставится вне модели')
    def test_not_create_mark_issue(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_haus)
        viewer_page.issue_btn.click()
        viewer_page.issue_add.click()
        viewer_page.mouse_dblclick(x=150, y=100, button='left')

        # Assert
        viewer_page.issue_details_window.assert_visibility(is_visible=False)


    @allure.title('Создать метку замечание')
    @pytest.mark.parametrize("test_title , test_text, x_coordinate",
                             [("Ш", "Тест тема 1.", 600),
                              ("Проверка ввода заголовка длиннее почти.", "Тест тема 2.", 615),
                              ("1234567890123456789012345678901234567890", "Тест тема 3.", 630),
                              ("Проверка ввода заголовка", "Тест тема 4.", 645),
                              ("Автотест текст 1", "Д", 660),
                              ("Автотест текст 2", "Проверочный текст для наполнения замечания", 675),
                              ("Автотест текст 3",
                                "Проверочный текст для наполнения замечания проверочный текст для наполнения замечания проверочный текст для наполнения замечания проверочный текст для наполнения замечания проверочный текст для наполнения замечания проверочный текст для наполнения з",
                               690),
                              ("Автотест текст 4",
                                "Проверочный текст для наполнения замечания проверочный текст для наполнения замечания проверочный текст для наполнения замечания проверочный текст для наполнения замечания проверочный текст для наполнения замечания проверочный текст для наполнения за",
                               705)
                              ],
                            )

    def test_create_issue(self, viewer_page, test_title, test_text, x_coordinate):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_haus)
        viewer_page.issue_btn.click()
        viewer_page.issue_add.click()
        viewer_page.mouse_dblclick(x=x_coordinate, y=500, button='left')
        today = str(dt.date.today())
        test_title = test_title
        # test_title = "Автотест "+today
        # test_text = "Содержание замечания из автотеста "+today
        test_text = test_text


        test_date = str(dt.date.today() + dt.timedelta(days=1))
        test_user = "Unigoda Salyami Shein"

        viewer_page.issue_title.fill(test_title)
        viewer_page.issue_text.fill(test_text)
        viewer_page.issue_date_fix.click()
        viewer_page.issue_date_fix.fill(test_date)
        viewer_page.issue_date_fix.press(key='Escape')
        viewer_page.issue_to_user.click()
        viewer_page.issue_first_user_in_list.click(to_user=test_user)
        viewer_page.issue_save.click()

        # Assert
        viewer_page.wait_request()
        viewer_page.issue_details_window.assert_visibility()
