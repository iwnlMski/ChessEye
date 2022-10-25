from typing import List
from PyQt6.QtCore import QObject
from custom_label import QLabelCustom
from const import FILEPATH_PREFIX, FILETYPE_EXTENSION

class BoardState():
    def __init__(self, list_of_tiles: List[QObject]):
        self.board_dict = self.generate_board_dict(list_of_tiles)


    def generate_board_dict(self, list_of_tiles: List[QObject]):
        dict_ = {}
        for tile in list_of_tiles:
            if isinstance(tile, QLabelCustom):
                dict_[tile.objectName().replace("label_", "")] = {
                    "piece": self.get_piece_name(tile)
                }
    
    def get_piece_name(self, item: QLabelCustom):
        return item.filename.replace(FILETYPE_EXTENSION, "").replace(FILEPATH_PREFIX, "")
