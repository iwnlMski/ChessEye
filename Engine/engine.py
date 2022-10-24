from enum import Enum
from typing import Optional


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Color(str, Enum):
    BLACK = 'b'
    WHITE = 'w'


class FigureType(str, Enum):
    PAWN = '♙'
    BISHOP = '♗'
    KNIGHT = '♘'
    ROOK = '♖'
    QUEEN = '♕'
    KING = '♔'


class Figure:
    def __init__(self, type: FigureType, color: Color):
        self.type = type
        self.color = color

    def __str__(self):
        return f'{bcolors.BOLD}{bcolors.OKCYAN if self.color == Color.BLACK else ""}{self.type}{bcolors.ENDC}'


class Coord:
    def __init__(self, row: int, col: int):
        self.row: int = row
        self.col: int = col

    @classmethod
    def name(cls, name: str):
        col = ord(name[0]) - 97
        row = int(name[1]) - 1
        return Coord(row, col)

    def __str__(self):
        return f'{chr(self.row + 97)}{self.col+1}'


class Field:
    def __init__(self, pos: Coord, figure: Optional[Figure] = None):
        self.position = pos
        self.figure = figure
        self.color = Color.BLACK if (
            pos.row % 2 + pos.col % 2 == 1) else Color.WHITE

    def __str__(self):
        return f'[{bcolors.OKBLUE if self.color == Color.BLACK else ""}{self.position}{bcolors.ENDC}{self.figure if self.figure else " "}]'


class Board:
    WIDTH: int = 8
    HEIGHT: int = 8

    def __init__(self):
        self.board = [[Field(Coord(row, col)) for row in range(
            Board.HEIGHT)] for col in range(Board.WIDTH)]

    def add_figure(self, pos: Coord, figure: Figure):
        self.board[pos.row][pos.col].figure = figure


def print_board(board: Board):
    for row in reversed(range(board.HEIGHT)):
        print("".join(str(f) for f in board.board[row]))


default_pieces = {
    Coord.name("a1"): Figure(FigureType.ROOK, Color.WHITE),
    Coord.name("b1"): Figure(FigureType.KNIGHT, Color.WHITE),
    Coord.name("c1"): Figure(FigureType.BISHOP, Color.WHITE),
    Coord.name("d1"): Figure(FigureType.QUEEN, Color.WHITE),
    Coord.name("e1"): Figure(FigureType.KING, Color.WHITE),
    Coord.name("f1"): Figure(FigureType.BISHOP, Color.WHITE),
    Coord.name("g1"): Figure(FigureType.KNIGHT, Color.WHITE),
    Coord.name("h1"): Figure(FigureType.ROOK, Color.WHITE),
    Coord.name("a2"): Figure(FigureType.PAWN, Color.WHITE),
    Coord.name("b2"): Figure(FigureType.PAWN, Color.WHITE),
    Coord.name("c2"): Figure(FigureType.PAWN, Color.WHITE),
    Coord.name("d2"): Figure(FigureType.PAWN, Color.WHITE),
    Coord.name("e2"): Figure(FigureType.PAWN, Color.WHITE),
    Coord.name("f2"): Figure(FigureType.PAWN, Color.WHITE),
    Coord.name("g2"): Figure(FigureType.PAWN, Color.WHITE),
    Coord.name("h2"): Figure(FigureType.PAWN, Color.WHITE),

    Coord.name("a8"): Figure(FigureType.ROOK, Color.BLACK),
    Coord.name("b8"): Figure(FigureType.KNIGHT, Color.BLACK),
    Coord.name("c8"): Figure(FigureType.BISHOP, Color.BLACK),
    Coord.name("d8"): Figure(FigureType.QUEEN, Color.BLACK),
    Coord.name("e8"): Figure(FigureType.KING, Color.BLACK),
    Coord.name("f8"): Figure(FigureType.BISHOP, Color.BLACK),
    Coord.name("g8"): Figure(FigureType.KNIGHT, Color.BLACK),
    Coord.name("h8"): Figure(FigureType.ROOK, Color.BLACK),
    Coord.name("a7"): Figure(FigureType.PAWN, Color.BLACK),
    Coord.name("b7"): Figure(FigureType.PAWN, Color.BLACK),
    Coord.name("c7"): Figure(FigureType.PAWN, Color.BLACK),
    Coord.name("d7"): Figure(FigureType.PAWN, Color.BLACK),
    Coord.name("e7"): Figure(FigureType.PAWN, Color.BLACK),
    Coord.name("f7"): Figure(FigureType.PAWN, Color.BLACK),
    Coord.name("g7"): Figure(FigureType.PAWN, Color.BLACK),
    Coord.name("h7"): Figure(FigureType.PAWN, Color.BLACK),
}


if __name__ == "__main__":
    board = Board()
    for pos, figure in default_pieces.items():
        board.add_figure(pos, figure)
    print_board(board)
