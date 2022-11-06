from enum import Enum


class Player:
    class Color(str, Enum):
        BLACK = 'Black Player'
        WHITE = 'White Player'

    def __init__(self, color: Color) -> None:
        self.color = color
        self.captured_pieces = []

    def __str__(self):
        return self.color
