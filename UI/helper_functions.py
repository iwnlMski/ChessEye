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
            if isinstance(obj, QLabelCustom) and obj.dragged_status:
                obj.dragged_status = False
                return obj

    @staticmethod
    def swap_two_labels(label_1: QLabelCustom, label_2: QLabelCustom) -> None:
        label_1_filename, label_2_filename = label_1.filename, label_2.filename

        label_1.setPixmap(label_2_filename)
        label_2.setPixmap(label_1_filename)
