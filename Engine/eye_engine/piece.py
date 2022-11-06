from enum import Enum

from .font import Font


class Piece:
    class Color(str, Enum):
        BLACK = 'BLACK'
        WHITE = 'WHITE'

    class Type(str, Enum):
        PAWN = '♙'
        BISHOP = '♗'
        KNIGHT = '♘'
        ROOK = '♖'
        QUEEN = '♕'
        KING = '♔'

    def __init__(self, piece_type: Type, color: Color):
        self.type = piece_type
        self.color = color
        self.history = []

    def __str__(self):
        return f'{Font.BLUE if self.color == Piece.Color.BLACK else Font.WHITE}{self.type}{Font.CLEAR}'
