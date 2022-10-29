from enum import Enum
from logging import error, basicConfig
from typing import List, Optional, Tuple


class Font(str, Enum):
    BLUE = '\033[94m'
    RED = "\x1b[31;1m"
    CLEAR = '\033[0m'


basicConfig(format=f"\t{Font.RED}%(message)s{Font.CLEAR}")


class Color(str, Enum):
    BLACK = 'BLACK'
    WHITE = 'WHITE'


class Piece(str, Enum):
    PAWN = '♙'
    BISHOP = '♗'
    KNIGHT = '♘'
    ROOK = '♖'
    QUEEN = '♕'
    KING = '♔'


class Pos(str, Enum):
    A1 = "a1"
    A2 = "a2"
    A3 = "a3"
    A4 = "a4"
    A5 = "a5"
    A6 = "a6"
    A7 = "a7"
    A8 = "a8"
    B1 = "b1"
    B2 = "b2"
    B3 = "b3"
    B4 = "b4"
    B5 = "b5"
    B6 = "b6"
    B7 = "b7"
    B8 = "b8"
    C1 = "c1"
    C2 = "c2"
    C3 = "c3"
    C4 = "c4"
    C5 = "c5"
    C6 = "c6"
    C7 = "c7"
    C8 = "c8"
    D1 = "d1"
    D2 = "d2"
    D3 = "d3"
    D4 = "d4"
    D5 = "d5"
    D6 = "d6"
    D7 = "d7"
    D8 = "d8"
    E1 = "e1"
    E2 = "e2"
    E3 = "e3"
    E4 = "e4"
    E5 = "e5"
    E6 = "e6"
    E7 = "e7"
    E8 = "e8"
    F1 = "f1"
    F2 = "f2"
    F3 = "f3"
    F4 = "f4"
    F5 = "f5"
    F6 = "f6"
    F7 = "f7"
    F8 = "f8"
    G1 = "g1"
    G2 = "g2"
    G3 = "g3"
    G4 = "g4"
    G5 = "g5"
    G6 = "g6"
    G7 = "g7"
    G8 = "g8"
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"
    H7 = "h7"
    H8 = "h8"


class Figure:
    def __init__(self, piece_type: Piece, color: Color):
        self.type = piece_type
        self.color = color
        self.history = []

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

    def capture(self, field_to):
        field_to.figure = None
        field_to.figure, self.figure = self.figure, field_to.figure
        field_to.figure.history.append(field_to)

    def __str__(self):
        return f'{Font.BLUE if self.color == Color.BLACK else Font.CLEAR}{self.position}{Font.CLEAR}{self.figure if self.figure else "_"} '


class Board:
    WIDTH: int = 8
    HEIGHT: int = 8

    def __init__(self, setup: List[Tuple[Pos, Figure]]):
        self.board = [[Field(Coord(row, col)) for row in range(
            Board.HEIGHT)] for col in range(Board.WIDTH)]

        for pos, figure in setup:
            self.add_figure(pos, figure)

    def add_figure(self, pos: Pos, figure: Figure):
        coord = Coord.from_pos(pos)
        field = self.board[coord.row][coord.col]
        figure.history.append(field)
        field.figure = figure

    def get_field(self, pos: Pos) -> Field:
        coord = Coord.from_pos(pos)
        return self.board[coord.row][coord.col]

    def move(self, field_from: Field, field_to: Field):
        moved_figure = field_from.figure
        if not moved_figure:
            raise RuntimeError(f"No figure in {field_from}")

        captured_figure = field_to.figure
        if captured_figure and captured_figure.color == moved_figure.color:
            raise RuntimeError(
                f"Unable to move figure {moved_figure} on top of another same color figure {captured_figure}")

        field_from.capture(field_to)

    def __str__(self):
        lines = []
        for row in reversed(range(self.HEIGHT)):
            lines.append("\t"+"".join(str(f) for f in self.board[row]))
        return "\n".join(lines)


default_pieces = [Piece.ROOK, Piece.KNIGHT, Piece.BISHOP, Piece.QUEEN, Piece.KING, Piece.BISHOP, Piece.KNIGHT,
                  Piece.ROOK, Piece.PAWN, Piece.PAWN, Piece.PAWN, Piece.PAWN, Piece.PAWN, Piece.PAWN, Piece.PAWN, Piece.PAWN]
white_fields = [Pos.A1, Pos.B1, Pos.C1, Pos.D1, Pos.E1, Pos.F1, Pos.G1,
                Pos.H1, Pos.A2, Pos.B2, Pos.C2, Pos.D2, Pos.E2, Pos.F2, Pos.G2, Pos.H2]
black_fields = [Pos.A8, Pos.B8, Pos.C8, Pos.D8, Pos.E8, Pos.F8, Pos.G8,
                Pos.H8, Pos.A7, Pos.B7, Pos.C7, Pos.D7, Pos.E7, Pos.F7, Pos.G7, Pos.H7]
default_board = list((pos, Figure(piece, Color.WHITE)) for pos, piece in zip(white_fields, default_pieces)) + \
    list((pos, Figure(piece, Color.BLACK))
         for pos, piece in zip(black_fields, default_pieces))


class Game:
    def __init__(self) -> None:
        self.history: List[Board] = []
        self.board: Board = Board(default_board)
        self.current_player_color: Color = Color.WHITE
        self.winner: Optional[Color] = None

    def valid_moves(self, field: Field, board: Board) -> List[Field]:
        figure = field.figure
        if not figure:
            raise RuntimeError(
                f"Field {field} does not contain a figure to move")

        moves = []
        # Implement move logic for all pieces
        if figure.type is Piece.PAWN:
            moves.append(board.get_field(Pos.A4))

        return moves

    def move_positions(self, from_position: Pos, to_position: Pos):
        return self.move_fields(self.board.get_field(from_position), self.board.get_field(to_position))

    def move_fields(self, from_field: Field, to_field: Field):
        from_figure = from_field.figure
        if not from_figure:
            raise RuntimeError(f"{from_field} does not have a figure to move")

        if from_figure.color is not self.current_player_color:
            raise RuntimeError(
                f"{self.current_player_color} tried to move other player {from_field}")

        to_figure = to_field.figure
        if to_figure and from_figure.color is to_figure.color:
            raise RuntimeError(
                f"{from_field} cannot move on top of a same color {to_field} piece")

        from_moves = self.valid_moves(from_field, self.board)
        if to_field not in from_moves:
            raise RuntimeError(
                f"{from_field} cannot move to {to_field}, available moves: {', '.join([str(f) for f in from_moves])}")

        self.board.move(from_field, to_field)
        self.current_player_color = Color.BLACK if self.current_player_color is Color.WHITE else Color.WHITE

    def __str__(self):
        return f'{self.board}\n\n{self.winner + " won!" if self.winner else self.current_player_color + " to move"}'


def read_move() -> Tuple[Pos, Pos]:
    move = input("Input move (eg. a2a4): ")
    if len(move) != 4:
        raise ValueError(f"Input {move} length invald")
    from_str = move[0:2]
    to_str = move[2:]
    try:
        from_position = Pos[from_str.upper()]
        to_position = Pos[to_str.upper()]
    except KeyError as key_error:
        raise ValueError(f"Position {key_error} is invalid") from KeyError
    return from_position, to_position


if __name__ == "__main__":
    game = Game()
    print(game)

    while not game.winner:
        try:
            from_pos, to_pos = read_move()
        except ValueError as value_error:
            error(f"Invalid input: {value_error}")

        try:
            game.move_positions(from_pos, to_pos)
        except RuntimeError as runtime_error:
            error(f"Error: {runtime_error}")
            continue

        print(game)
