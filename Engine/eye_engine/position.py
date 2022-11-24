from __future__ import annotations
from typing import Optional, Tuple


class Position:
    a_ascii_offset = 97

    def __init__(self, name: str):
        self.name = name.lower()
        if len(name) != 2:
            raise ValueError(f"Invalid position length: {name}")
        coord = self.to_coord(name)
        if not coord:
            raise ValueError(f"Invalid position name {name}")
        self.col: int = coord[0]
        self.row: int = coord[1]

    @classmethod
    def to_coord(cls, name: str) -> Optional[Tuple[int, int]]:
        col: int = ord(name.lower()[0]) - cls.a_ascii_offset
        if not 0 <= col < 8:
            return None

        row: int = int(name[1]) - 1
        if not 0 <= row < 8:
            return None

        return col, row

    @classmethod
    def to_name(cls, col: int, row: int) -> Optional[str]:
        name = chr(col + cls.a_ascii_offset) + str(row+1)
        return name if (col, row) == cls.to_coord(name) else None

    def __hash__(self) -> int:
        return hash(repr(self))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        if not isinstance(other, Position):
            return NotImplemented
        return self.row == other.row and self.col == other.col and self.name == other.name
