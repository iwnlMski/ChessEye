from typing import Dict, List, Optional, Tuple, Callable
from .position import Position
from .piece import Piece


rook_offsets = [[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)],
                [(0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7)],
                [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)],
                [(-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0)]]

bishop_offsets = [[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)],
                  [(-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7)],
                  [(1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7)],
                  [(-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7)]]

queen_offsets = rook_offsets + bishop_offsets

knight_offsets = [[(2, 1)], [(-2, -1)], [(-2, 1)], [(2, -1)], [(1, 2)], [(-1, -2)], [(-1, 2)], [(1, -2)]]
king_offsets = [[(0, 1)], [(0, -1)], [(1, 1)], [(-1, -1)], [(1, 0)], [(-1, 0)], [(-1, 1)], [(1, -1)]]
pawn_capture_offsets = [[(1, 1)], [(1, -1)]]
pawn_move_offsets = [[(1, 0)], [(2, 0)]]


def capture(piece: Piece, target: Piece):
    return piece.is_opponent(target)


def move(_: Piece, target: Piece):
    return target.is_empty()


def move_or_capture(piece: Piece, target: Piece):
    return capture(piece, target) or move(piece, target)


def move_pawn(piece: Piece, target: Piece):
    default_row = 1 if piece.is_white() else 6
    return move(piece, target) if (piece.position.row is default_row) or abs(target.position.row - piece.position.row) == 1 else False


moves: Dict[Piece.Type, Dict[Callable[[Piece, Piece], bool], List[List[Tuple[int, int]]]]] = {
    Piece.Type.PAWN: {move_pawn: pawn_move_offsets, capture: pawn_capture_offsets},
    Piece.Type.KNIGHT: {move_or_capture: knight_offsets},
    Piece.Type.KING: {move_or_capture: king_offsets},
    Piece.Type.ROOK: {move_or_capture: rook_offsets},
    Piece.Type.BISHOP: {move_or_capture: bishop_offsets},
    Piece.Type.QUEEN: {move_or_capture: queen_offsets}
}


def try_apply_offset(position: Position, offset: Tuple[int, int], mirror_offset: bool = False) -> Optional[Position]:
    direction: int = -1 if mirror_offset else 1
    row = position.row + direction * offset[0]
    col = position.col + direction * offset[1]
    if 0 <= row <= 7 and 0 <= col <= 7 and (name := Position.to_name(col, row)):
        return Position(name)
    return None
