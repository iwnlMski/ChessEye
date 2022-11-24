from itertools import chain
from typing import Dict, List, Optional, Set
from .position import Position
from .piece import Piece
from .moves import moves, try_apply_offset
from .position_constants import *  # pylint: disable=unused-wildcard-import, wildcard-import
from .piece_constants import *  # pylint: disable=unused-wildcard-import, wildcard-import


class Board:
    def __init__(self, setup: List[Piece]):
        self.board = [[Piece(Position(chr(col) + str(row))) for col in range(ord('a'), ord('h') + 1)]
                      for row in range(1, 8 + 1)]

        for field in setup:
            self.set_field(field)

    @classmethod
    def create_default(cls):
        return cls([
            Piece(A1, ROOK, WHITE), Piece(B1, KNIGHT, WHITE), Piece(C1, BISHOP, WHITE), Piece(D1, QUEEN, WHITE), Piece(E1, KING, WHITE), Piece(F1, BISHOP, WHITE), Piece(G1, KNIGHT, WHITE), Piece(H1, ROOK, WHITE), Piece(A2, PAWN, WHITE), Piece(B2, PAWN, WHITE), Piece(C2, PAWN, WHITE), Piece(D2, PAWN, WHITE), Piece(E2, PAWN, WHITE), Piece(F2, PAWN, WHITE), Piece(G2, PAWN, WHITE), Piece(H2, PAWN, WHITE), Piece(
                A8, ROOK, BLACK), Piece(B8, KNIGHT, BLACK), Piece(C8, BISHOP, BLACK), Piece(D8, QUEEN, BLACK), Piece(E8, KING, BLACK), Piece(F8, BISHOP, BLACK), Piece(G8, KNIGHT, BLACK), Piece(H8, ROOK, BLACK), Piece(A7, PAWN, BLACK), Piece(B7, PAWN, BLACK), Piece(C7, PAWN, BLACK), Piece(D7, PAWN, BLACK), Piece(E7, PAWN, BLACK), Piece(F7, PAWN, BLACK), Piece(G7, PAWN, BLACK), Piece(H7, PAWN, BLACK),
        ])

    def get_field(self, position: Position) -> Piece:
        return self.board[position.row][position.col]

    def set_field(self, piece: Piece) -> None:
        field = self.get_field(piece.position)
        field.type = piece.type
        field.color = piece.color

    def __str__(self):
        lines = []
        for row in reversed(range(0, 8)):
            lines.append("\t"+"".join(str(f) for f in self.board[row]))
        return "\n".join(lines)

    def __repr__(self) -> str:
        return self.__str__()

    def move(self, piece_position: Position, target_position: Position, color: Piece.Color) -> Optional[Piece]:
        piece = self.get_field(piece_position)
        if piece.is_empty():
            raise RuntimeError(f"{piece} does not have a figure to move")

        if piece.color != color:
            raise RuntimeError(f"{color} tried to move other player {piece}")

        target = self.get_field(target_position)
        if piece.is_same(target):
            raise RuntimeError(f"tried to move {piece} on top of same color {target}")

        valid = self.valid_moves(piece_position)
        if target_position not in valid:
            raise RuntimeError(f"Invalid move, available: {valid}")

        piece.move_to(target)
        return None

    def valid_moves(self, piece_position: Position) -> Set[Position]:
        piece = self.get_field(piece_position)
        if piece.is_empty():
            raise RuntimeError(f"{piece} does not have a figure to move")

        valid: Set[Position] = set()
        for filter_fn, move_lines in moves[piece.type].items():
            for lines in move_lines:
                for offset in lines:
                    position = try_apply_offset(piece_position, offset, mirror_offset=piece.is_black())
                    if not position:
                        break
                    target = self.get_field(position)
                    if filter_fn(piece, target):
                        valid.add(position)

                    if target.has_piece():
                        break
        return valid

    def all_moves(self, piece_color: Optional[Piece.Color] = None, piece_type: Optional[Piece.Type] = None, position: Optional[Position] = None) -> Dict[Position, List[Position]]:
        move_map = {}
        for field in filter(lambda p: p.has_piece() and (not piece_color or p.color == piece_color) and (not piece_type or p.type == piece_type) and (not position or p.position == position), chain.from_iterable(self.board)):
            valid_moves = self.valid_moves(field.position)
            if valid_moves:
                move_map[field.position] = valid_moves
        return move_map
