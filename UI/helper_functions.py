from const import TILE_SIZE, LabelType
from typing import List, Union
from PyQt6.QtCore import QObject
from custom_label import QLabelCustom


class LabelHelperFunctions():
    @staticmethod
    def get_board_tile_from_position(x: int, y: int, list_of_objects: List[QObject]) -> Union[QLabelCustom, None]:
        for obj in list_of_objects:
            if LabelType.TILE.value in obj.objectName() and x in range(obj.x(), obj.x() + TILE_SIZE) and y in range(obj.y(), obj.y() + TILE_SIZE):
                return obj

    @staticmethod
    def get_label_by_dragged_status(list_of_objects: List[QObject]) -> Union[QLabelCustom, None]:
        for obj in list_of_objects:
            if LabelType.PIECE_COUNTER.value not in obj.objectName() and obj.dragged_status:
                obj.dragged_status = False
                return obj

    @staticmethod
    def swap_two_labels(label_1: QLabelCustom, label_2: QLabelCustom) -> None:
        label_1_filename, label_2_filename = label_1.filename, label_2.filename

        label_1.setPixmap(label_2_filename)
        label_2.setPixmap(label_1_filename)

    @staticmethod
    def add_piece_from_stack(label_1: QLabelCustom, label_2: QLabelCustom, list_of_objects: List[QObject]):
        piece_name = label_1.filename.replace(
            "../img/", "").replace(".png", "")
        for obj in list_of_objects:
            if obj.objectName() == LabelType.PIECE_COUNTER.value + piece_name:
                if int(obj.text()) > 0:
                    label_2.setPixmap(label_1.filename)
                    obj.setText(str(int(obj.text()) - 1))
                return

    @staticmethod
    def delete_piece_from_board(label_1: QLabelCustom):
        label_1.setPixmap("")

    @staticmethod
    def update_piece_stack(label_1: QLabelCustom, list_of_objects: List[QObject]):
        piece_name = label_1.filename.replace(
            "../img/", "").replace(".png", "")
        for obj in list_of_objects:
            if obj.objectName() == LabelType.PIECE_COUNTER.value + piece_name:
                obj.setText(str(int(obj.text()) + 1))
