from enum import Enum
from typing import List

from .piece import Piece
from .font import Font


class Player:
    class Color(str, Enum):
        BLACK = '♙Black Player♙'
        WHITE = '♙White Player♙'

    def __init__(self, color: Piece.Color) -> None:
        self.piece_color: Piece.Color = color
        self.captured_pieces: List[Piece] = []

    def owns(self, piece: Piece):
        return self.piece_color == piece.color

    def owns_black(self) -> bool:
        return self.piece_color == Piece.Color.BLACK

    def owns_white(self) -> bool:
        return self.piece_color == Piece.Color.WHITE

    def __str__(self):
        return f'{Font.BLUE + "♙Black Player♙" if self.owns_black() else Font.WHITE + "♙White Player♙"}{Font.CLEAR}'

    def __repr__(self) -> str:
        return self.__str__()
