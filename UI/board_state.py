from typing import List
from PyQt6.QtCore import QObject
from custom_label import QLabelCustom
from const import FILEPATH_PREFIX, FILETYPE_EXTENSION
import json

class BoardState():
    def __init__(self, list_of_tiles: List[QObject]):
        self.pieces_on_board = len(list(filter(lambda x: isinstance(x, QLabelCustom) and x.filename, list_of_tiles)))
        self.board = self.generate_board_dict(list_of_tiles)

    def generate_board_dict(self, list_of_tiles: List[QObject]):
        dict_ = {}
        for tile in list_of_tiles:
            if isinstance(tile, QLabelCustom):
                dict_[tile.objectName().replace("label_", "")] = {
                    "piece": self.get_piece_name(tile)
                }
        return dict_
            
    
    def get_piece_name(self, item: QLabelCustom):
        return item.filename.replace(FILETYPE_EXTENSION, "").replace(FILEPATH_PREFIX, "")

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
                sort_keys=True, indent=4)
