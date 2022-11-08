from typing import List
from .board import Board
from .position import Position
from .player import Player
from .piece import Piece
from .moves import moves


class Engine:
    @staticmethod
    def move(piece_position: Position, target_position: Position, color: Player.Color, board: Board):
        piece_field = board.get_field(piece_position)
        piece = piece_field.piece
        if not piece:
            raise RuntimeError(f"{piece_field} does not have a figure to move")

        if (piece.color == Piece.Color.WHITE) != (color == Player.Color.WHITE):
            raise RuntimeError(f"{color} tried to move other player {piece_field}")

        target_field = board.get_field(target_position)
        target_piece = target_field.piece
        if target_piece and (target_piece.color == Piece.Color.WHITE) == (color == Player.Color.WHITE):
            raise RuntimeError(f"tried to move {piece_field} on top of same color {target_field}")

    @staticmethod
    def valid_moves(piece_position: Position, board: Board) -> List[Position]:
        piece_field = board.get_field(piece_position)
        piece = piece_field.piece
        if not piece:
            raise RuntimeError(f"{piece_field} does not have a figure to move")

        valid = []
        for filter_fn, move_lines in moves[piece.type].items():
            for line in move_lines:
                for offset in line:
                    try:
                        offset_sign = 1 if piece.color is Piece.Color.WHITE else -1
                        position = piece_position + (offset * offset_sign)
                        field = board.get_field(position)
                        if filter_fn(piece_field, field):
                            valid.append(position)
                        else:
                            break
                    except ValueError:
                        break
        return valid
