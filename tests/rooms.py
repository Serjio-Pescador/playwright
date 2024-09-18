import allure
import pytest
from singleton import BaseUrlSingleton
from pages.viewer_page import TooltipName, SortedListRooms
from static.test_data import TestData
from PIL import Image
from io import BytesIO


@pytest.mark.regress
@allure.story('Помещения')
class TestRooms:

    @allure.title('Check page URL')
    def test_valid_url(self, viewer_page):
        # Arrange
        expected_url = BaseUrlSingleton.get_base_url()
        # Act

        # Assert
        viewer_page.assert_url_window_eql(expected_url)


    @allure.title('Помещения тултип кнопки')
    def test_rooms_btn_tt(self, viewer_page):
        # Act
        viewer_page.rooms.hover()
        tooltip_text = TooltipName.tt_rooms.value

        # Assert
        viewer_page.tooltip.assert_visibility(tooltip_text=tooltip_text)
        viewer_page.tooltip.assert_text_eql(tooltip_text=tooltip_text, text=tooltip_text)


    @allure.title('Помещения окно списка')
    def test_rooms_list_window(self, viewer_page):
        # Act
        viewer_page.rooms.click()

        # Assert
        viewer_page.rooms_list_window.assert_visibility()


    @allure.title('Помещения заголовок окна списка')
    def test_rooms_list_title(self, viewer_page):
        # Act
        viewer_page.rooms.click()
        viewer_page.rooms_list_window.get_text()
        title = TooltipName.tt_rooms.value

        # Assert
        viewer_page.rooms_list_window_title.assert_text_eql(title=title, text=title)


    @allure.title('Помещения виден список')
    def test_rooms_list_shown(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_small_set)
        viewer_page.rooms.click()
        row = 1

        # Assert
        viewer_page.room_list.assert_visibility(row_room=row)


    @allure.title('Выбор помещения в списке открывает окно свойств и помещение на модели')
    def test_room_choose(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_small_set)
        viewer_page.rooms.click()
        row = 1
        viewer_page.room_list.click(row_room=row)

        # Assert
        viewer_page.properties_window.assert_visibility()
        viewer_page.test_screenshot(image_snapshot, timeout=5000)


    @allure.title('Проверка модели без помещений')
    def test_no_room_for_choice(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_without_room)
        viewer_page.rooms.click()
        viewer_page.rooms_list_window.assert_visibility()
        row = 1

        # Assert
        viewer_page.room_list.assert_visibility(row_room=row, is_visible=False)
        viewer_page.test_screenshot(image_snapshot, timeout=5000)


    @allure.title('Проверка сортировки помещений в списке по номерам и названиям')
    def test_rooms_list_sorted(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        test_sorted_list = [SortedListRooms.list_rooms_OldBerezin.replace('\n','').replace('  ','')]

        # Assert
        viewer_page.room_list_full.assert_visibility()
        viewer_page.room_list_full.assert_text_eql(text=test_sorted_list)


    @allure.title('Чек-бокс номер в списке помещений отключить')
    def test_rooms_list_checkbox_number(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        viewer_page.room_list_full.assert_visibility()
        viewer_page.rooms_list_checkbox_numbers.set_checked(status=False)
        viewer_page.rooms_list_chbx_numbers.assert_is_checked(is_checked=False)
        test_sorted_list = [SortedListRooms.list_rooms_OldBerezin_without_numbers.replace('\n', '').replace('  ', '')]

        # Assert
        viewer_page.rooms_list_chbx_names.assert_is_checked()
        viewer_page.room_list_full.assert_text_eql(text=test_sorted_list)

    @allure.title('Выключить чек-бокс Имя в помещениях')
    def test_rooms_list_checkbox_name(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        viewer_page.room_list_full.assert_visibility()
        viewer_page.rooms_list_checkbox_names.set_checked(status=False)
        viewer_page.rooms_list_chbx_names.assert_is_checked(is_checked=False)
        viewer_page.rooms_list_chbx_numbers.assert_is_checked()
        test_sorted_list = [SortedListRooms.list_rooms_OldBerezin_without_names.replace('\n', '').replace('  ', '')]

        # Assert
        viewer_page.room_list_full.assert_text_eql(text=test_sorted_list)


    @allure.title('Помещения первый чек-бокс активный')
    def test_rooms_list_checkboxes_first(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        viewer_page.room_list_full.assert_visibility()
        viewer_page.rooms_list_checkbox_names.set_checked(status=False)
        viewer_page.rooms_list_chbx_names.assert_is_checked(is_checked=False)
        viewer_page.rooms_list_chbx_numbers.click()

        # Assert
        viewer_page.rooms_list_chbx_numbers.assert_is_checked(is_checked=True)


    @allure.title('Помещения второй чек-бокс активный')
    def test_rooms_list_checkboxes_second(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        viewer_page.room_list_full.assert_visibility()
        viewer_page.rooms_list_chbx_numbers.set_checked(status=False)
        viewer_page.rooms_list_chbx_numbers.assert_is_checked(is_checked=False)
        viewer_page.rooms_list_chbx_names.click()

        # Assert
        viewer_page.rooms_list_chbx_names.assert_is_checked(is_checked=True)


    @allure.title('Оба чек-бокса в помещениях можно поочередно прокликать')
    def test_rooms_list_checkboxes(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        viewer_page.room_list_full.assert_visibility()
        viewer_page.rooms_list_chbx_numbers.set_checked(status=False)
        viewer_page.rooms_list_chbx_numbers.assert_is_checked(is_checked=False)
        viewer_page.rooms_list_chbx_numbers.set_checked(status=True)
        viewer_page.rooms_list_chbx_names.set_checked(status=False)
        viewer_page.rooms_list_chbx_names.assert_is_checked(is_checked=False)

        # Assert
        viewer_page.rooms_list_chbx_names.set_checked(status=True)

    @allure.title('Поиск в списке помещений пустое по умолчанию')
    def test_rooms_list_search_empty(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        viewer_page.room_list_full.assert_visibility()

        # Assert
        viewer_page.room_list_search.get_text()
        viewer_page.room_list_search.assert_text_eql("")

    @allure.title('Поиск в списке помещений по обоим полям')
    def test_rooms_list_search_both(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        viewer_page.room_list_full.assert_visibility()
        viewer_page.room_list_search.fill("4")
        test_sorted_list = [SortedListRooms.list_rooms_OldBerezin_search_4.replace('\n', '').replace('  ', '')]

        # Assert
        viewer_page.room_list_full.assert_text_eql(text=test_sorted_list)
        viewer_page.test_screenshot(image_snapshot, timeout=5000)


    @allure.title('Поиск в списке помещений по номеру')
    def test_rooms_list_search_numbers(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        viewer_page.room_list_full.assert_visibility()
        viewer_page.rooms_list_checkbox_names.click()
        viewer_page.room_list_search.fill("4")
        test_sorted_list = [SortedListRooms.list_rooms_OldBerezin_search_4_in_numbers.replace('\n', '').replace('  ', '')]

        # Assert
        viewer_page.room_list_full.assert_text_eql(text=test_sorted_list)
        viewer_page.test_screenshot(image_snapshot, timeout=5000)


    @allure.title('Поиск в списке помещений по имени')
    def test_rooms_list_search_names(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        viewer_page.room_list_full.assert_visibility()
        viewer_page.rooms_list_checkbox_numbers.click()
        viewer_page.room_list_search.fill("11")
        test_sorted_list = [SortedListRooms.list_rooms_OldBerezin_search_11_in_names.replace('\n', '').replace('  ', '')]

        # Assert
        viewer_page.room_list_full.assert_text_eql(text=test_sorted_list)
        viewer_page.test_screenshot(image_snapshot, timeout=5000)


    @allure.title('Rooms List активная строка')
    def test_rooms_list_active(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        viewer_page.rooms_list_chbx_numbers.set_checked(status=False)
        viewer_page.rooms_list_chbx_numbers.assert_is_checked(is_checked=False)
        test_room = 'Лестничная клетка 3'
        viewer_page.rooms_list_room.click(room_in_list=test_room)

        # Assert
        viewer_page.rooms_list_active.assert_visibility(room_in_list=test_room)
        viewer_page.test_screenshot(image_snapshot, timeout=5000)


    @allure.title('Название помещения в свойствах')
    def test_room_properties(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        viewer_page.rooms_list_chbx_numbers.set_checked(status=False)
        viewer_page.rooms_list_chbx_numbers.assert_is_checked(is_checked=False)
        first_room = 'Лестничная клетка 3'
        viewer_page.rooms_list_room.click(room_in_list=first_room)

        # Assert
        viewer_page.room_in_properties.assert_visibility(name_room=first_room)


    @allure.title('Rooms List активная строка')
    def test_rooms_properties_change(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        viewer_page.rooms_list_chbx_numbers.set_checked(status=False)
        viewer_page.rooms_list_chbx_numbers.assert_is_checked(is_checked=False)
        first_room = 'Лестничная клетка 3'
        viewer_page.rooms_list_room.click(room_in_list=first_room)
        viewer_page.room_in_properties.assert_visibility(name_room=first_room)
        second_room = 'Офисное помещение 4'
        viewer_page.rooms_list_room.click(room_in_list=second_room)

        # Assert
        viewer_page.test_screenshot(image_snapshot, timeout=5000)


    @allure.title('Помещения закрытие свойств')
    def test_rooms_properties_close(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        room_name = 'Офисное помещение 3'
        room = f'1.3 {room_name}'
        viewer_page.rooms_list_room.click(room_in_list=room)
        viewer_page.room_in_properties.assert_visibility(name_room=room_name)
        viewer_page.rooms_properties_close.click()

        # Assert
        viewer_page.room_in_properties.assert_visibility(is_visible=False, name_room=room_name)
        viewer_page.rooms_list_active.assert_visibility(is_visible=False, room_in_list=room_name)
        viewer_page.test_screenshot(image_snapshot, timeout=5000)


    @allure.title('Помещение есть вкладка паспорт')
    def test_room_tab_passport(self, viewer_page):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        viewer_page.rooms.click()
        room_name = 'Офисное помещение 3'
        room = f'1.3 {room_name}'
        viewer_page.rooms_list_room.click(room_in_list=room)

        # Assert
        viewer_page.room_in_properties.assert_visibility(name_room=room_name)
        viewer_page.room_passport.assert_visibility()


    @allure.title('Помещение вкладка паспорт')
    def test_room_passport(self, viewer_page, image_snapshot):
        # Act

        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        viewer_page.rooms.click()
        room_name = 'Офисное помещение 3'
        room = f'1.3 {room_name}'
        viewer_page.rooms_list_room.click(room_in_list=room)
        viewer_page.room_in_properties.assert_visibility(name_room=room_name)
        viewer_page.room_passport.click()

        # Assert
        viewer_page.test_screenshot(image_snapshot, timeout=3000)


    @allure.title('Помещение вкладка паспорт разделы')
    def test_room_passport_titles(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        viewer_page.rooms.click()
        room = '1.3 Офисное помещение 3'
        viewer_page.rooms_list_room.click(room_in_list=room)
        viewer_page.room_passport.click()
        test_quantity = 5+1  # заголовок в паспорте в таком же div как и разделы

        # Assert
        viewer_page.room_passport_titles.count(count=test_quantity)


    @allure.title('Помещение вкладка паспорт смена на другое помещение')
    def test_room_passport_change(self, viewer_page, ):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        viewer_page.rooms.click()
        viewer_page.rooms_list_chbx_names.set_checked(status=False)
        viewer_page.rooms_list_chbx_names.assert_is_checked(is_checked=False)
        roomnumber1 = '0.15'
        viewer_page.rooms_list_room.click(room_in_list=roomnumber1)
        viewer_page.roomnumber_in_passport.assert_visibility(roomnumber=roomnumber1)
        roomnumber2 = '1.3'
        viewer_page.rooms_list_room.click(room_in_list=roomnumber2)

        # Assert
        viewer_page.roomnumber_in_passport.assert_visibility(roomnumber=roomnumber2)


    @allure.title('Помещение оборудование в помещение (по скрину)')
    def test_equipments_in_room(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_house_set)
        viewer_page.rooms.click()
        viewer_page.rooms_list_chbx_names.set_checked(status=False)
        viewer_page.rooms_list_chbx_names.assert_is_checked(is_checked=False)
        roomnumber1 = '1.7'
        viewer_page.rooms_list_room.click(room_in_list=roomnumber1)

        # Assert
        viewer_page.test_screenshot(image_snapshot, timeout=3000)


    @allure.title('Помещение появление слайдера прозрачности')
    def test_slider_opacity(self, viewer_page,):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_small_set)
        viewer_page.rooms.click()
        room_number = '1 Помещение'
        viewer_page.rooms_list_room.click(room_in_list=room_number)

        # Assert
        viewer_page.slider_opacity.assert_visibility()


    @allure.title('Помещение слайдера прозрачности увеличение')
    def test_slider_left(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_small_set)
        viewer_page.rooms.click()
        room_number = '1 Помещение'
        viewer_page.rooms_list_room.click(room_in_list=room_number)
        while True:
            value = viewer_page.slider_handle.get_attribute(name='aria-valuenow')
            if value =="10":
                break
            viewer_page.slider_handle.press(key='ArrowLeft')

        # Assert
        viewer_page.test_screenshot(image_snapshot, timeout=10000)


    @allure.title('Помещение слайдера прозрачности уменьшение')
    def test_slider_right(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        room_number = '1.4 Помещение'
        viewer_page.rooms_list_room.click(room_in_list=room_number)
        while True:
            value = viewer_page.slider_handle.get_attribute(name='aria-valuenow')
            if value =="90":
                break
            viewer_page.slider_handle.press(key='ArrowRight')

        # Assert
        viewer_page.test_screenshot(image_snapshot, timeout=12000)


    @allure.title('Помещение слайдера прозрачности уменьшение')
    def test_slider_stay_value(self, viewer_page, image_snapshot):
        # Act
        viewer_page.local_upload(ifc=TestData.ifc_Berezin)
        viewer_page.rooms.click()
        check_value = "20"
        room_number1 = '1.4 Помещение'
        viewer_page.rooms_list_room.click(room_in_list=room_number1)
        while True:
            value = viewer_page.slider_handle.get_attribute(name='aria-valuenow')
            if value == check_value:
                break
            viewer_page.slider_handle.press(key='ArrowLeft')
        room_number2 = '2.4 Санузел'
        viewer_page.rooms_list_room.click(room_in_list=room_number2)

        # Assert
        viewer_page.slider_handle.to_have_attribute(name='aria-valuenow', value=check_value)
        viewer_page.test_screenshot(image_snapshot, timeout=10000)