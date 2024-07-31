from typing import Union

import allure

from pages.components.base_element import PageElement


class UploadFiles(PageElement):

    @property
    def _type_of(self):
        return 'UploadFiles'

    def set_files(self, path: Union[str, list], **kwargs):
        with allure.step(f'Загрузить файлы в {self._type_of}: "{self._format_name(**kwargs)}".'):
            self._find_element(**kwargs).set_input_files(path)

    def delete_files(self, **kwargs):
        with allure.step(f'Удалить загруженные файлы в {self._type_of}: "{self._format_name(**kwargs)}".'):
            self.set_files(path=[], **kwargs)
