from ctypes import BigEndianStructure
from .field import Field
from .position import Position as Offset
from .piece import Piece


def capture(piece_field: Field, target_field: Field):
    target_piece = target_field.piece
    piece = piece_field.piece
    return target_piece and piece and (target_field.color is not piece_field.color)


def move(field_from: Field, field_to: Field):
    return field_from.piece and not field_to.piece


def move_or_capture(field_from: Field, field_to: Field):
    return capture(field_from, field_to) or move(field_from, field_to)


def pawn_double(field_from: Field, field_to: Field):
    piece = field_from.piece
    if not piece:
        raise ValueError("No piece for pawn double forward move")
    row = 1 if piece.color is Piece.Color.WHITE else 6
    return move(field_from, field_to) if field_from.position.row is row else False


rook_offsets = [[Offset(0, 1), Offset(0, 2), Offset(0, 3), Offset(0, 4), Offset(0, 5), Offset(0, 6), Offset(0, 7)],
                [Offset(0, -1), Offset(0, -2), Offset(0, -3), Offset(
                    0, -4), Offset(0, -5), Offset(0, -6), Offset(0, -7)],
                [Offset(1, 0), Offset(2, 0), Offset(3, 0), Offset(
                    4, 0), Offset(5, 0), Offset(6, 0), Offset(7, 0)],
                [Offset(-1, 0), Offset(-2, 0), Offset(-3, 0), Offset(
                    -4, 0), Offset(-5, 0), Offset(-6, 0), Offset(-7, 0)]]

bishop_offsets = [[Offset(1, 1), Offset(2, 2), Offset(3, 3), Offset(4, 4), Offset(5, 5), Offset(6, 6), Offset(7, 7)],
                  [Offset(-1, -1), Offset(-2, -2), Offset(-3, -3), Offset(-4, -4),
                   Offset(-5, -5), Offset(-6, -6), Offset(-7, -7)],
                  [Offset(1, -1), Offset(2, -2), Offset(3, -3), Offset(4, -4),
                   Offset(5, -5), Offset(6, -6), Offset(7, -7)],
                  [Offset(-1, 1), Offset(-2, 2), Offset(-3, 3), Offset(-4, 4), Offset(-5, 5), Offset(-6, 6), Offset(-7, 7)]]

knight_offsets = [[Offset(2, 1)], [Offset(-2, -1)], [Offset(-2, 1)],
                  [Offset(2, -1)], [Offset(1, 2)], [Offset(-1, -2)], [Offset(-1, 2)], [Offset(1, -2)]]

king_offsets = [[Offset(0, 1)], [Offset(0, -1)], [Offset(1, 1)],
                [Offset(-1, -1)], [Offset(1, 0)], [Offset(-1, 0)], [Offset(-1, 1)], [Offset(1, -1)]]

queen_offsets = rook_offsets + bishop_offsets

moves = {
    Piece.Type.PAWN: {move: [[Offset(1, 0)]], pawn_double: [[Offset(2, 0)]]},
    Piece.Type.KNIGHT: {move_or_capture: knight_offsets},
    Piece.Type.KING: {move_or_capture: king_offsets},
    Piece.Type.ROOK: {move_or_capture: rook_offsets},
    Piece.Type.BISHOP: {move_or_capture: bishop_offsets},
    Piece.Type.QUEEN: {move_or_capture: queen_offsets}
}
