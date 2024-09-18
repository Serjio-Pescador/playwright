from pages.components.tooltip import Tooltip
from pages.components.button import Button
from pages.components.input import Input
from pages.components.slider import Slider
from pages.components.checkbox import CheckBox
from pages.components.text import Text
from pages.base_page import BasePage
import enum, glob, os


class TooltipName(enum.Enum):

    tt_files = 'файлы'
    tt_local = 'локально'
    tt_back = 'назад'
    tt_demo = 'демо'
    tt_reset = 'Сбросить модель'
    tt_rooms = 'Помещения'
    tt_issues = 'Замечания'


class SortedListRooms():

    list_rooms_OldBerezin = """
    1.1 Офисное помещение 2
    1.2 Лестничная клетка 3
    1.3 Офисное помещение 3
    1.4 Помещение
    1.5 Санузел1.6 Санузел
    1.7 Коридор
    1.8 Лестничная клетка 2
    1.9 Лестничная клетка 1
    1.10 Офисное помещение 4
    1.11 Офисное помещение 1
    2.1 Офисное помещение 7
    2.2 Офисное помещение 8
    2.3 Офисное помещение 9
    2.4 Санузел
    2.5 Офисное помещение 6
    2.6 Офисное помещение 10
    2.7 Коридор
    2.8 Офисное помещение 11
    2.9 Офисное помещение 5
    2.10 Офисное помещение 12"""

    list_rooms_OldBerezin_without_numbers = """
    Коридор
    Коридор
    Лестничная клетка 1
    Лестничная клетка 2
    Лестничная клетка 3
    Офисное помещение 1
    Офисное помещение 2
    Офисное помещение 3
    Офисное помещение 4
    Офисное помещение 5
    Офисное помещение 6
    Офисное помещение 7
    Офисное помещение 8
    Офисное помещение 9
    Офисное помещение 10
    Офисное помещение 11
    Офисное помещение 12
    Помещение
    Санузел
    Санузел
    Санузел"""

    list_rooms_OldBerezin_without_names = '1.11.21.31.41.51.61.71.81.91.101.112.12.22.32.42.52.62.72.82.92.10'
    list_rooms_OldBerezin_search_4 = '1.4 Помещение1.10 Офисное помещение 42.4 Санузел'
    list_rooms_OldBerezin_search_4_in_numbers = '1.42.4'
    list_rooms_OldBerezin_search_11_in_names = 'Офисное помещение 11'

    list_rooms_house = """
    0.11 Котельная
    0.12 Коридор
    0.13 Подвальное  помещение
    0.14 Подвальное  помещение
    0.15 Коридор
    0.17 Подвальное  помещение
    0.18 ИТП
    0.19 Подвальное  помещение
    1.1 Офисное помещение 2
    1.2 Лестничная клетка 3
    1.3 Офисное помещение 3
    1.4 Тамбур
    1.5 Санузел
    1.6 Санузел
    1.7 Коридор
    1.8 Лестничная клетка 2
    1.9 Лестничная клетка 1
    1.10 Офисное помещение 4
    1.11 Офисное помещение 1
    2.1 Кабинет директора
    2.2 Зона ожидания
    2.3 Отдел снабжения
    2.4 Санузел
    2.5 Зона ожидания
    2.6 Зона ожидания
    2.7 Коридор
    2.8 Офисное помещение 11
    2.9 Кабинет руководителя
    2.10 Бухгалтерия
    3.1 Чердачное помещение"""


class ViewerPage(BasePage):
    def __init__(self):
        super().__init__()

        # меню и окно список
        self.tooltip = Tooltip(locator="//*[@class='ant-tooltip-inner' and text()='{tooltip_text}']", name='ТТ {tooltip_text}')
        self.files = Button(locator="//*[@data-testid='menu-btn-files']", name='Files')
        self.local = Button(locator="//*[@data-testid='menu-btn-files-local']", name='Local')
        self.back = Button(locator="//*[@data-testid='menu-btn-back']", name='Back')
        self.demo = Button(locator="//*[@data-testid='menu-btn-files-demo']", name='Demo')
        self.reset = Button(locator="//*[@data-testid='menu-btn-files-reset']", name='Reset')
        self.rooms = Button(locator="//*[@id='root']/div/div/button[2]", name='Rooms')
        self.rooms_list_window = Text(locator="//div[@class='ant-popover-content']", name='Rooms List Window')
        self.rooms_list_window_title = Text(locator="//p[@class='container__title menu-title' and text()='{title}']", name='Окно с заголовком {title}')
        self.room_list = Button(locator="(//*[@class='layer-button'])[{row_room}]", name='{row_room} Помещение в списке')
        self.rooms_list_room = Text(locator="//*[@class='layer-button' and text()='{room_in_list}']", name='Выбор помещения в списке')
        self.room_list_full = Text(locator="//*[@class='rooms-list']", name="Full room list")


        # окно свойств, паспорта
        self.properties_window = Text(locator="//div[@class='ant-card ant-card-bordered WorkflowMenuWindow css-dev-only-do-not-override-98ntnt']", name='Помещение')
        self.rooms_list_checkbox_numbers = CheckBox(locator="(//*[@class='ant-checkbox-wrapper ant-checkbox-wrapper-checked css-dev-only-do-not-override-98ntnt'])[1]", name="номера помещений")
        self.rooms_list_checkbox_names = CheckBox(locator="(//*[@class='ant-checkbox-wrapper ant-checkbox-wrapper-checked css-dev-only-do-not-override-98ntnt'])[2]", name="названия помещений")
        self.rooms_list_chbx_numbers = CheckBox(locator="(//*[@class='ant-checkbox-input'])[1]", name="номера помещений")
        self.rooms_list_chbx_names = CheckBox(locator="(//*[@class='ant-checkbox-input'])[2]", name="названия помещений")
        self.room_list_search = Input(locator="//*[@class='ant-input css-dev-only-do-not-override-98ntnt']", name="Поле поиска")
        self.rooms_list_active = Text(locator="//*[@class='rooms-list-item active']//*[@class='layer-button' and text()='{room_in_list}']", name="Активная вкладка")
        self.room_in_properties = Text(locator="//p[text()='{name_room}']", name='Rooms Properties {name_room}')
        self.rooms_properties_close = Button(locator="//div[@class='ant-card-extra']", name="Закрытие окна свойств")
        self.room_passport = Button(locator="//*[@id='rc-tabs-0-tab-passport']", name="Вкладка паспорта помещения")
        self.roomnumber_in_passport = Text(locator="//*[@class='ant-descriptions-item-content']//span[text()='{roomnumber}']", name='Rooms Passport {roomnumber}')
        self.slider_opacity = Button(locator="//div[@class='opacity-slider']",
                                    name="Слайдер прозрачности помещения")
        self.slider_handle = Slider(locator="//div[@class='ant-slider-handle']", name="Ручка слайдера прозрачности")
        self.room_passport_titles = Text(locator="//div[@class='ant-descriptions-title']", name="Заголовки разделов в Паспорте помещения")


        # Чек-листы помещений
        self.room_checklist_tab = Button(locator="//*[@id='rc-tabs-0-tab-finishing']", name="Вкладка чек-листа помещения")
        self.room_checklist_create = Button(locator="//button[@class='ant-btn css-dev-only-do-not-override-98ntnt ant-btn-default create-room-checklist-btn']", name="Создать чек-лист помещения")
        self.room_checklist_rows = Text(locator="//tr[@class='ant-table-row ant-table-row-level-0']", name="Разделы чек-листа помещения")
        self.room_checklist = Text(locator="//div[@class='ant-space css-dev-only-do-not-override-98ntnt ant-space-vertical ant-space-gap-row-small ant-space-gap-col-small check-list-table-space']", name="Чек-лист помещения")
        self.room_checklist_table_btn = Button(locator="//button[@class='ant-btn css-dev-only-do-not-override-98ntnt ant-btn-default show-table-btn']", name='открытие сводная таблица')
        self.room_checklist_table = Text(locator="//div[@class='ant-modal-content']", name='Cводная таблица')
        self.room_checklist_download_btn_csv = Button(locator="//button[@class='ant-btn css-dev-only-do-not-override-98ntnt ant-btn-default check-list-download-file-btn'][1]", name='скачать таблицу в csv')
        self.room_checklist_download_btn_pdf = Button(locator="//button[@class='ant-btn css-dev-only-do-not-override-98ntnt ant-btn-default check-list-download-file-btn'][2]", name='скачать таблицу в pdf')
        self.room_checklist_download_btn_all = Button(locator="//button[@class='ant-btn css-dev-only-do-not-override-98ntnt ant-btn-default check-list-download-all-files-btn']", name='скачать таблицу все форматы')
        self.room_checklist_row = Text(locator="//tr[@class='ant-table-row ant-table-row-level-0'][{row}]", name="{row} раздел чек-листа помещения")
        self.room_checklist_resolve_panel = Button(locator="(//div[@class='accept-solution-btn-panel'])[1]", name='приемка или отказ')
        self.checklist_fact_quantity_first = Input(locator="(//div[@class='input-number-container fact-units-input']//input)[1]", name="Фактическое значение для первого пункта")
        self.checklist_back_from_chapter = Button(locator="//button[@class='ant-btn css-dev-only-do-not-override-98ntnt ant-btn-text check-list-btn-back']", name="выхода из раздела чек-листа")
        self.checklist_comment_first = Input(locator='//*[@id="comment"]', name="Комментарий для первого пункта")
        self.checklist_refuse = Button(locator="(//button[@class='ant-btn css-dev-only-do-not-override-98ntnt ant-btn-default status-btn refuse-btn'])[{point}]", name="отклонить {point} пункт чек-листа")
        self.checklist_refused = Button(locator="(//button[@class='ant-btn css-dev-only-do-not-override-98ntnt ant-btn-default status-btn refuse-btn refused'])[{point}]", name="отказано {point} пункт чек-листа")
        self.checklist_accept = Button(locator="(//button[@class='ant-btn css-dev-only-do-not-override-98ntnt ant-btn-default status-btn accept-btn'])[{point}]", name="принять {point} пункт чек-листа")
        self.checklist_accepted = Button(locator="(//button[@class='ant-btn css-dev-only-do-not-override-98ntnt ant-btn-default status-btn accept-btn approve'])[{point}]", name="принято {point} пункт чек-листа")
        self.room_checklist_content = Text(locator="//*[@class='window-content']", name="Контент пунктов чек-листа")
        self.room_checklist_success = Text(locator="//div[@class='success-checked-text room-check-list-progress-title']", name="Шильдик Все пункты чек-листа отмечены")
        self.row_accepted = Text(locator="//*[@class='check-icon green']", name="Зеленая галочка пункт принят ")
        self.row_refused = Text(locator="//*[@class='cross-icon']", name="Красный крестик пункт отклонен")
        self.row_partial = Text(locator="//*[@class='check-icon yellow']", name="Желтая галочка пункт разные статусы")
        self.title_partial_tick = Text(locator="//*[@class='header-icon partial']", name="Желтая галочка заголовок")

        # Замечания
        self.issue_btn = Button(locator="(//*[@class='css-dev-only-do-not-override-98ntnt ant-float-btn menu-float-button menu-float-btn ant-float-btn-default ant-float-btn-square'])[4]", name="Замечания")
        self.issue_list_close = Button(locator="//*[@class='ant-btn css-dev-only-do-not-override-98ntnt ant-btn-default ant-btn-icon-only close-popover-btn no-border-btn']", name="Закрыть список")

        self.issue_add = Button(locator="//button[@data-testid='add-issue-marker']", name="Добавить замечание")
        self.issue_details_window = Text(locator="//*[@data-testid='issue-popup-card']", name="Окно деталей и создания замечания")
        self.issue_title = Input(locator="(//*[@class='ant-input-affix-wrapper ant-input-textarea-affix-wrapper ant-input-affix-wrapper-lg css-dev-only-do-not-override-98ntnt ant-input-textarea-allow-clear ant-input-outlined'])//*[@placeholder='Тема']", name="Тема замечания")
        self.issue_text = Input(locator="(//*[@class='ant-input-affix-wrapper ant-input-textarea-affix-wrapper ant-input-affix-wrapper-lg css-dev-only-do-not-override-98ntnt ant-input-textarea-allow-clear ant-input-outlined'])//*[@placeholder='Введите текст замечания']", name="Текст замечания")
        self.issue_date_fix = Input(locator="//*[@id='dateToFix']", name="Дата устранения")
        self.issue_to_user = Input(locator="//*[@id='toUser']", name="Кому")
        self.issue_first_user_in_list = Input(locator="(//*[@class='ant-select-item-option-content'])[text()='{to_user}']", name="Кому в списке {to_user}")
        self.issue_save = Button(locator="//*[@data-testid='add-issue-submit-btn']", name="Сохранить")


    def local_upload(self, ifc):
        self.files.click()
        self.local.click()
        self.ifc_full_upload(ifc)
        self.reset.to_be_enabled()
        self.back.click()