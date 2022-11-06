from __future__ import annotations


class Position:
    def __init__(self, row: int, col: int):
        self.row: int = row
        self.col: int = col

    a_ascii_offset = 97

    @classmethod
    def from_name(cls, name: str) -> Position:
        if len(name) != 2:
            raise ValueError(f"Position name {name} length invalid")

        col = ord(name.lower()[0]) - cls.a_ascii_offset
        if not (0 <= col < 8):
            raise ValueError(f"Invalid column value {col}")
        row = int(name[1]) - 1
        if not (0 <= row < 8):
            raise ValueError(f"Invalid row value {row}")

        return Position(row, col)

    @classmethod
    def to_name(cls, position: Position) -> str:
        return f'{chr(position.col + cls.a_ascii_offset)}{position.row+1}'

    def __str__(self) -> str:
        return Position.to_name(self)