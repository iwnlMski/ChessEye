from __future__ import annotations
from enum import Enum

from .position import Position
from .font import Font


class Piece:
    class Color(str, Enum):
        BLACK = 'BLACK'
        WHITE = 'WHITE'
        NONE = 'NONE'

    class Type(str, Enum):
        PAWN = '♙'
        BISHOP = '♗'
        KNIGHT = '♘'
        ROOK = '♖'
        QUEEN = '♕'
        KING = '♔'
        NONE = '_'

    def __init__(self, position: Position, piece_type: Type = Type.NONE, color: Color = Color.NONE):
        self.type = piece_type
        self.color = color
        self.position = position

    def is_opponent(self, target: Piece) -> bool:
        return not target.is_empty() and not self.is_same(target)

    def is_same(self, target: Piece) -> bool:
        return not target.is_empty() and self.color == target.color

    def is_empty(self) -> bool:
        return self.type == Piece.Type.NONE

    def has_piece(self) -> bool:
        return not self.is_empty()

    def is_white(self) -> bool:
        return self.color == Piece.Color.WHITE

    def is_black(self) -> bool:
        return self.color == Piece.Color.BLACK

    def remove_piece(self):
        t, c = Piece.Type.NONE, Piece.Color.NONE
        self.type, t = t, self.type
        self.color, c = c, self.color
        return t, c

    def move_to(self, target: Piece):
        t, c = target.remove_piece()
        self.color, target.color = target.color, self.color
        self.type, target.type = target.type, self.type
        return t, c

    def __str__(self):
        field_color = Font.BLUE if (self.position.row + self.position.col) % 2 else Font.WHITE
        return f'{field_color}{self.position}{Font.CLEAR}{Font.BLUE if self.is_black() else Font.WHITE}{self.type}{Font.CLEAR}'

    def __repr__(self) -> str:
        return self.__str__()
