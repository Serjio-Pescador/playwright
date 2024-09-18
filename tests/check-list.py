import allure
import pytest, os
from singleton import BaseUrlSingleton
from static.test_data import TestData
from conftest import viewer_delete_checklist


def create_check_list(viewer_page, room_name: str=None):
    viewer_page.rooms.click()
    viewer_page.rooms_list_room.click(room_in_list=room_name)
    viewer_page.room_checklist_tab.click()
    viewer_page.room_checklist_create.click()

@pytest.mark.regress
@allure.epic('ЧЕК-ЛИСТЫ')
@allure.story('чек-листы помещений')
class TestRoomChecklists:

    @allure.title('Check page URL')
    def test_valid_url(self, viewer_page):
        # Arrange
        expected_url = BaseUrlSingleton.get_base_url()

        # Assert
        viewer_page.assert_url_window_eql(expected_url)


    @allure.title('Помещение есть вкладка чек-лист')
    def test_room_checklist_tab(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_small_set)
        viewer_page.rooms.click()
        room = f'1 Помещение'
        viewer_page.rooms_list_room.click(room_in_list=room)

        # Assert
        viewer_page.room_checklist_tab.assert_visibility()


    @allure.title('Нет вкладки чек-лист')
    def test_no_room_checklist_tab(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_haus)
        viewer_page.rooms.click()
        viewer_page.rooms_list_chbx_numbers.set_checked(status=False)
        viewer_page.rooms_list_chbx_numbers.assert_is_checked(is_checked=False)
        room_name = 'Flur'
        viewer_page.rooms_list_room.click(room_in_list=room_name)

        # Assert
        viewer_page.room_checklist_tab.assert_visibility(is_visible=False)



    @allure.title('Чек-лист кнопка создание')
    def test_room_checklist_create(self, viewer_page, viewer_delete_checklist):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_small_set)
        viewer_page.rooms.click()
        room = '1 Помещение'
        viewer_page.rooms_list_room.click(room_in_list=room)
        viewer_page.room_checklist_tab.click()
        viewer_page.room_checklist_create.click()

        # Assert
        viewer_page.room_checklist.assert_visibility()


    @allure.title('Чек-лист количество разделов отделки')
    def test_room_checklist_rows(self, viewer_page, viewer_delete_checklist):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_small_set)
        room_name = '1 Помещение'
        create_check_list(viewer_page, room_name=room_name)

        # Assert
        viewer_page.room_checklist_rows.count(count=5)


    @allure.title('Чек-лист помещения открыть сводную таблицу')
    def test_room_checklist_table_open(self, viewer_page, viewer_delete_checklist):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_small_set)
        room_name = '1 Помещение'
        create_check_list(viewer_page, room_name=room_name)
        viewer_page.room_checklist_table_btn.click()

        # Assert
        viewer_page.room_checklist_table.assert_visibility()


    @allure.title('Чек-лист помещения скачать сводную таблицу csv')
    @pytest.mark.parametrize('file_type', ["csv", "pdf", "all"]
    )
    def test_room_checklist_table_download(self, viewer_page, viewer_delete_checklist, file_type):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_small_set)
        room_name = '1 Помещение'
        create_check_list(viewer_page, room_name=room_name)

        # Assert
        viewer_page.download_type(file_type)



    @allure.title('Сравнение разделов в паспорте и чек-листе')
    def test_room_passport_and_checklist_chapters(self, viewer_page, viewer_delete_checklist):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        room_name = '1.3 Офисное помещение 3'
        create_check_list(viewer_page, room_name=room_name)
        chapters = 5

        # Assert
        viewer_page.room_checklist_rows.count(count=chapters)
        viewer_page.room_passport.click()
        viewer_page.room_passport_titles.count(count=chapters+1) # заголовок в паспорте в таком же div как и разделы


    @allure.title('Чек-лист помещения открыть первый раздел')
    def test_room_checklist_chapter_choose(self, viewer_page, viewer_delete_checklist):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_small_set)
        room_name = '1 Помещение'
        create_check_list(viewer_page, room_name=room_name)
        row = 1
        viewer_page.room_checklist_row.click(row=row)

        # Assert
        viewer_page.room_checklist_resolve_panel.assert_visibility()


    @allure.title('Чек-лист помещения изменить факт.значение первый раздел первый пункт')
    def test_room_checklist_change_fact_quantity(self, viewer_delete_checklist, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_small_set)
        room_name = '1 Помещение'
        create_check_list(viewer_page, room_name=room_name)
        row = 1
        viewer_page.room_checklist_row.click(row=row)
        viewer_page.checklist_fact_quantity_first.fill("13,54")
        viewer_page.wait_request()
        viewer_page.checklist_back_from_chapter.click()
        viewer_page.room_checklist_row.click(row=row)

        # Assert
        viewer_page.checklist_fact_quantity_first.to_have_attribute(name='value', value="13,54")


    @allure.title('Чек-лист помещения комментарий первый раздел первый пункт')
    def test_room_checklist_make_comment(self, viewer_delete_checklist, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_small_set)
        room_name = '1 Помещение'
        create_check_list(viewer_page, room_name=room_name)
        row = 1
        test_data_comment = "Test from Autotests"
        viewer_page.room_checklist_row.click(row=row)
        viewer_page.checklist_comment_first.fill(test_data_comment)
        viewer_page.wait_request()
        viewer_page.checklist_back_from_chapter.click()
        viewer_page.room_checklist_row.click(row=row)

        # Assert
        viewer_page.checklist_comment_first.assert_text_eql(test_data_comment)


    @allure.title('Чек-лист помещения отклонить единственный пункт крестик в заголовке')
    def test_room_checklist_decline_single(self, viewer_delete_checklist, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        room_name = '1.6 Санузел'
        create_check_list(viewer_page, room_name=room_name)
        row = 5
        point = 1
        viewer_page.room_checklist_row.click(row=row)
        viewer_page.room_checklist_resolve_panel.to_be_enabled()
        viewer_page.checklist_refuse.click(point=point)
        viewer_page.wait_request()

        # Assert
        viewer_page.checklist_refused.assert_visibility(point=point)
        viewer_page.test_screenshot(image_snapshot, timeout=7000)


    @allure.title('Чек-лист помещения отклонить единственный пункт крестик в разделах')
    def test_room_checklist_decline_single_cross(self, viewer_delete_checklist, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        room_name = '1.6 Санузел'
        create_check_list(viewer_page, room_name=room_name)
        row = 5
        viewer_page.room_checklist_row.click(row=row)
        viewer_page.room_checklist_resolve_panel.to_be_enabled()
        viewer_page.checklist_refuse.click(point=1)
        viewer_page.wait_request()
        viewer_page.checklist_refused.assert_visibility(point=1)
        viewer_page.checklist_back_from_chapter.click()
        viewer_page.wait_request()

        # Assert
        viewer_page.row_refused.assert_visibility()
        viewer_page.test_screenshot(image_snapshot, diff=0.8)


    @allure.title('Чек-лист помещения принять единственный пункт зеленая галка в заголовке')
    def test_room_checklist_accept_single(self, viewer_delete_checklist, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        room_name = '1.6 Санузел'
        create_check_list(viewer_page, room_name=room_name)
        row = 5
        point = 1
        viewer_page.room_checklist_row.click(row=row)
        viewer_page.room_checklist_resolve_panel.to_be_enabled()
        viewer_page.checklist_accept.click(point=point)
        viewer_page.wait_request()

        # Assert
        viewer_page.checklist_accepted.assert_visibility(point=point)
        viewer_page.test_screenshot(image_snapshot, timeout=7000)


    @allure.title('Галочка чек-лист помещения принять единственный пункт зеленая галка в разделах')
    def test_room_checklist_accept_single_tick(self, viewer_delete_checklist, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        room_name = '1.6 Санузел'
        create_check_list(viewer_page, room_name=room_name)
        row = 5
        point = 1
        viewer_page.room_checklist_row.click(row=row)
        viewer_page.room_checklist_resolve_panel.to_be_enabled()
        viewer_page.checklist_accept.click(point=point)
        viewer_page.wait_request()
        viewer_page.checklist_accepted.assert_visibility(point=point)
        viewer_page.checklist_back_from_chapter.click()
        viewer_page.wait_request()

        # Assert
        viewer_page.row_accepted.assert_visibility()
        viewer_page.test_screenshot(image_snapshot, timeout=8000)


    @allure.title('Чек-лист помещения 2 пункта: принять и отклонить желтая галочка в заголовке')
    def test_room_checklist_accept_decline_yellow_tick(self, viewer_delete_checklist, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        room_name = '1.7 Коридор'
        create_check_list(viewer_page, room_name=room_name)
        row = 4
        viewer_page.room_checklist_row.click(row=row)
        viewer_page.wait_request()
        viewer_page.room_checklist_resolve_panel.to_be_enabled()
        viewer_page.checklist_refuse.click(point=2)
        viewer_page.wait_request()
        viewer_page.checklist_refused.assert_visibility(point=1)
        viewer_page.checklist_accept.click(point=1)
        viewer_page.wait_request()
        viewer_page.checklist_accepted.assert_visibility(point=1)
        for i in range(50):
            viewer_page.room_checklist_content.press(key='ArrowUp')

        # Assert
        viewer_page.title_partial_tick.assert_visibility()
        viewer_page.test_screenshot(image_snapshot, timeout=5000)


    @allure.title('Чек-лист помещения 2 пункта: принять и отклонить желтая галочка в разделах')
    def test_room_checklist_accept_decline_part(self, viewer_delete_checklist, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        room_name = '1.7 Коридор'
        create_check_list(viewer_page, room_name=room_name)
        row = 4
        viewer_page.room_checklist_row.click(row=row)
        viewer_page.wait_request()
        viewer_page.room_checklist_resolve_panel.to_be_enabled()
        viewer_page.checklist_refuse.click(point=2)
        viewer_page.wait_request()
        viewer_page.checklist_refused.assert_visibility(point=1)
        viewer_page.checklist_accept.click(point=1)
        viewer_page.wait_request()
        viewer_page.checklist_accepted.assert_visibility(point=1)
        for i in range(50):
            viewer_page.room_checklist_content.press(key='ArrowUp')
        viewer_page.checklist_back_from_chapter.click()

        # Assert
        viewer_page.row_partial.assert_visibility()
        viewer_page.test_screenshot(image_snapshot, timeout=5000)


    @allure.title('Чек-лист помещения 2 пункта (часть): принять и отклонить нет желтой галочки в заголовке')
    def test_room_checklist_accept_decline_part_no_yellow(self, viewer_delete_checklist, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        room_name = '1.7 Коридор'
        create_check_list(viewer_page, room_name=room_name)
        row = 2
        viewer_page.room_checklist_row.click(row=row)
        viewer_page.wait_request()
        viewer_page.room_checklist_resolve_panel.to_be_enabled()
        viewer_page.checklist_refuse.click(point=1,timeout=500)
        viewer_page.checklist_refused.assert_visibility(point=1)
        viewer_page.checklist_accept.click(point=2,timeout=500)
        viewer_page.checklist_accepted.assert_visibility(point=1)
        viewer_page.checklist_accept.click(point=3,timeout=500)
        viewer_page.checklist_accepted.assert_visibility(point=2)
        for i in range(50):
            viewer_page.room_checklist_content.press(key='ArrowUp')

        # Assert
        viewer_page.title_partial_tick.assert_visibility(is_visible=False)
        viewer_page.test_screenshot(image_snapshot, timeout=5000)


    @allure.title('Чек-лист помещения 2 пункта (часть): принять и отклонить нет желтой галочки')
    def test_room_checklist_accept_decline_part_no_marks(self, viewer_delete_checklist, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        room_name = '1.7 Коридор'
        create_check_list(viewer_page, room_name=room_name)
        row = 2
        viewer_page.room_checklist_row.click(row=row)
        viewer_page.wait_request()
        viewer_page.room_checklist_resolve_panel.to_be_enabled()
        viewer_page.checklist_refuse.click(point=1,timeout=500)
        viewer_page.checklist_refused.assert_visibility(point=1)
        viewer_page.checklist_accept.click(point=2,timeout=500)
        viewer_page.checklist_accepted.assert_visibility(point=1)
        viewer_page.checklist_accept.click(point=3,timeout=500)
        viewer_page.checklist_accepted.assert_visibility(point=2)
        for i in range(50):
            viewer_page.room_checklist_content.press(key='ArrowUp')
        viewer_page.checklist_back_from_chapter.click()
        viewer_page.wait_request()

        # Assert
        viewer_page.row_partial.assert_visibility(is_visible=False)
        viewer_page.test_screenshot(image_snapshot, timeout=5000)


    @allure.title('Чек-лист помещения принять все 5 типов, сообщение все проверено!')
    def test_room_checklist_accept_all(self, viewer_delete_checklist, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        room_name = '0.15 Коридор'
        create_check_list(viewer_page, room_name=room_name)
        total_point = 5
        viewer_page.room_checklist_row.click(row=1)
        viewer_page.wait_request()
        viewer_page.room_checklist_resolve_panel.to_be_enabled()
        for i in range(total_point):
            viewer_page.checklist_accept.click(point=1)
            viewer_page.wait_request()
            viewer_page.checklist_accepted.assert_visibility(point=1)
        viewer_page.checklist_back_from_chapter.click()

        # Assert
        viewer_page.room_checklist_success.assert_visibility()
        viewer_page.test_screenshot(image_snapshot, timeout=5000)


    @allure.title('Чек-лист помещения отклонить все 5 типов, сообщение все проверено!')
    def test_room_checklist_decline_all(self, viewer_delete_checklist, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        room_name = '0.15 Коридор'
        create_check_list(viewer_page, room_name=room_name)
        total_point = 5
        viewer_page.room_checklist_row.click(row=1)
        viewer_page.wait_request()
        viewer_page.room_checklist_resolve_panel.to_be_enabled()
        for i in range(total_point):
            viewer_page.checklist_refuse.click(point=1)
            viewer_page.wait_request()
            viewer_page.checklist_refused.assert_visibility(point=1)
        viewer_page.checklist_back_from_chapter.click()

        # Assert
        viewer_page.room_checklist_success.assert_visibility()
        viewer_page.test_screenshot(image_snapshot, timeout=5000)
