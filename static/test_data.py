from pages.base_page import BasePage
import glob

class TestData():

    # 3D модели отдельные или наборы файлов
    ifc_house_set = glob.glob("./static/house/*")          # средняя есть всё
    ifc_small_set = glob.glob("./static/small/*")          # маленькая есть всё
    ifc_haus = "./static/AC20-FZK-Haus.ifc"                # маленькая с помещениями
    ifc_Berezin = "./static/OldBerezin.ifc"                # средняя с помещениями
    ifc_without_room = "./static/aisc_sculpture_brep.ifc"  # без помещений
