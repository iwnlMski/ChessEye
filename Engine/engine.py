from enum import Enum
from logging import error, warning
import logging
from typing import List, Optional, Tuple


class Font:
    BLUE = '\033[94m'
    RED = "\x1b[31;1m"
    CLEAR = '\033[0m'


logging.basicConfig(
    format=f"\t{Font.RED}%(message)s{Font.CLEAR}")


class Color(str, Enum):
    BLACK = 'b'
    WHITE = 'w'


class Piece(str, Enum):
    PAWN = '♙'
    BISHOP = '♗'
    KNIGHT = '♘'
    ROOK = '♖'
    QUEEN = '♕'
    KING = '♔'


class Pos(str, Enum):
    a1 = "a1"
    a2 = "a2"
    a3 = "a3"
    a4 = "a4"
    a5 = "a5"
    a6 = "a6"
    a7 = "a7"
    a8 = "a8"
    b1 = "b1"
    b2 = "b2"
    b3 = "b3"
    b4 = "b4"
    b5 = "b5"
    b6 = "b6"
    b7 = "b7"
    b8 = "b8"
    c1 = "c1"
    c2 = "c2"
    c3 = "c3"
    c4 = "c4"
    c5 = "c5"
    c6 = "c6"
    c7 = "c7"
    c8 = "c8"
    d1 = "d1"
    d2 = "d2"
    d3 = "d3"
    d4 = "d4"
    d5 = "d5"
    d6 = "d6"
    d7 = "d7"
    d8 = "d8"
    e1 = "e1"
    e2 = "e2"
    e3 = "e3"
    e4 = "e4"
    e5 = "e5"
    e6 = "e6"
    e7 = "e7"
    e8 = "e8"
    f1 = "f1"
    f2 = "f2"
    f3 = "f3"
    f4 = "f4"
    f5 = "f5"
    f6 = "f6"
    f7 = "f7"
    f8 = "f8"
    g1 = "g1"
    g2 = "g2"
    g3 = "g3"
    g4 = "g4"
    g5 = "g5"
    g6 = "g6"
    g7 = "g7"
    g8 = "g8"
    h1 = "h1"
    h2 = "h2"
    h3 = "h3"
    h4 = "h4"
    h5 = "h5"
    h6 = "h6"
    h7 = "h7"
    h8 = "h8"


class Figure:
    def __init__(self, type: Piece, color: Color):
        self.type = type
        self.color = color

    def __str__(self):
        return f'{Font.BLUE if self.color == Color.BLACK else ""}{self.type}{Font.CLEAR}'


class Coord:
    a_ascii_offset = 97

    def __init__(self, row: int, col: int):
        self.row: int = row
        self.col: int = col

    @classmethod
    def from_pos(cls, pos: Pos):
        col = ord(pos[0]) - cls.a_ascii_offset
        row = int(pos[1]) - 1
        return Coord(row, col)

    def __str__(self):
        return f'{chr(self.row + self.a_ascii_offset)}{self.col+1}'


class Field:
    def __init__(self, pos: Coord, figure: Optional[Figure] = None):
        self.position = pos
        self.figure = figure
        self.color = Color.BLACK if (pos.row + pos.col) % 2 else Color.WHITE

    def __str__(self):
        return f'{Font.BLUE if self.color == Color.BLACK else ""}{self.position}{Font.CLEAR}{self.figure if self.figure else "_"} '


class Board:
    WIDTH: int = 8
    HEIGHT: int = 8

    def __init__(self, setup: List[Tuple[Pos, Figure]] = []):
        self.board = [[Field(Coord(row, col)) for row in range(
            Board.HEIGHT)] for col in range(Board.WIDTH)]

        for pos, figure in setup:
            self.add_figure(pos, figure)

    def add_figure(self, pos: Pos, figure: Figure):
        coord = Coord.from_pos(pos)
        self.board[coord.row][coord.col].figure = figure

    def get_field(self, pos: Pos) -> Field:
        coord = Coord.from_pos(pos)
        return self.board[coord.row][coord.col]

    def move(self, pos: Pos, to: Pos) -> bool:
        field_from = self.get_field(pos)
        moved_figure = field_from.figure
        if not moved_figure:
            warning(f"No figure in {pos}")
            return False

        field_to = self.get_field(to)
        captured_figure = field_to.figure
        if captured_figure and captured_figure.color == moved_figure.color:
            warning(
                f"Unable to move figure {pos} on top of another same color figure {to}")
            return False

        field_to.figure = None
        field_to.figure, field_from.figure = field_from.figure, field_to.figure

        return True


def print_board(board: Board):
    for row in reversed(range(board.HEIGHT)):
        print("\t"+"".join(str(f) for f in board.board[row]))


default_pieces = [Piece.ROOK, Piece.KNIGHT, Piece.BISHOP, Piece.QUEEN, Piece.KING, Piece.BISHOP, Piece.KNIGHT,
                  Piece.ROOK, Piece.PAWN, Piece.PAWN, Piece.PAWN, Piece.PAWN, Piece.PAWN, Piece.PAWN, Piece.PAWN, Piece.PAWN]
white_fields = [Pos.a1, Pos.b1, Pos.c1, Pos.d1, Pos.e1, Pos.f1, Pos.g1,
                Pos.h1, Pos.a2, Pos.b2, Pos.c2, Pos.d2, Pos.e2, Pos.f2, Pos.g2, Pos.h2]
black_fields = [Pos.a8, Pos.b8, Pos.c8, Pos.d8, Pos.e8, Pos.f8, Pos.g8,
                Pos.h8, Pos.a7, Pos.b7, Pos.c7, Pos.d7, Pos.e7, Pos.f7, Pos.g7, Pos.h7]
default_board = list((pos, Figure(piece, Color.WHITE)) for pos, piece in zip(white_fields, default_pieces)) + \
    list((pos, Figure(piece, Color.BLACK))
         for pos, piece in zip(black_fields, default_pieces))


def read_move() -> Tuple[Optional[Pos], Optional[Pos]]:
    move = input("Input move (eg. a2a4): ")
    if len(move) != 4:
        error(f"Input {move} length invald")
        return None, None
    from_str = move[0:2]
    to_str = move[2:]
    try:
        from_pos = Pos[from_str]
        to_pos = Pos[to_str]
    except KeyError as ex:
        error(f"Position {ex} is invalid")
        return None, None
    return from_pos, to_pos


if __name__ == "__main__":
    board = Board(default_board)
    print_board(board)

    while True:
        from_pos, to_pos = read_move()
        if not from_pos or not to_pos:
            continue

        board.move(from_pos, to_pos)
        print_board(board)
