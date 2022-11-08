from .field import Field
from .position import Position


class Board:
    WIDTH: int = 8
    HEIGHT: int = 8

    def __init__(self):
        self.board = [[Field(Position(row, col), Field.Color.WHITE if row % 2 == col % 2 else Field.Color.BLACK) for col in range(
            Board.HEIGHT)] for row in range(Board.WIDTH)]

    def get_field(self, position: Position) -> Field:
        if not (0 <= position.row < self.HEIGHT and 0 <= position.col < self.WIDTH):
            raise ValueError(f"Invalid get_field position {position}")

        return self.board[position.row][position.col]

    def add_piece(self, position, piece):
        self.get_field(position).piece = piece

    def __str__(self):
        lines = []
        for row in reversed(range(self.HEIGHT)):
            lines.append("\t"+"".join(str(f) for f in self.board[row]))
        return "\n".join(lines)
