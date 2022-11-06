from enum import Enum
from typing import Optional

from .font import Font
from .piece import Piece
from .position import Position


class Field:
    class Color(str, Enum):
        BLACK = 'BLACK'
        WHITE = 'WHITE'

    def __init__(self, position: Position, color: Color = Color.WHITE):
        self.color: Field.Color = color
        self.position: Position = position
        self.piece: Optional[Piece] = None

    def __str__(self):
        return f'{Font.BLUE if self.color == Field.Color.BLACK else Font.CLEAR}{self.position}{Font.CLEAR}{self.piece if self.piece else "_"}'
