from const import TILE_SIZE
from typing import List, Union
from PyQt6.QtCore import QObject
from custom_label import QLabelCustom

class LabelHelperFunctions():
    @staticmethod
    def get_label_by_position(x: int, y: int, list_of_objects: List[QObject]) -> Union[QLabelCustom, None]:
        for obj in list_of_objects:
            if isinstance(obj, QLabelCustom) and x in range(obj.x(), obj.x() + TILE_SIZE) and y in range(obj.y(), obj.y() + TILE_SIZE):
                return obj

    @staticmethod
    def get_label_by_dragged_status(list_of_objects: List[QObject]) -> Union[QLabelCustom, None]:
        for obj in list_of_objects:
            if isinstance(obj, QLabelCustom) and obj.get_dragged_status():
                obj.set_dragged_status(False)
                return obj

    @staticmethod
    def swap_two_labels(label_1: QLabelCustom, label_2: QLabelCustom) -> None:
        label_1.move(*label_2.get_start_pos())
        label_2.move(*label_1.get_start_pos())

        label_1_name = label_1.objectName()
        label_2_name = label_2.objectName()

        label_1.setObjectName(label_2_name)
        label_2.setObjectName(label_1_name)

        label_1.set_bg_color()
        label_2.set_bg_color()

        label_2.update_start_pos()
        label_1.update_start_pos()
