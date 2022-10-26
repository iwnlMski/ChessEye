from enum import Enum

TILE_SIZE = 60

class PieceImage(Enum):
    WHITE_PAWN = "../img/white_pawn.png"
    WHITE_ROOK = "../img/white_rook.png"
    WHITE_KNIGHT = "../img/white_knight.png"
    WHITE_BISHOP = "../img/white_bishop.png"
    WHITE_QUEEN = "../img/white_queen.png"
    WHITE_KING = "../img/white_king.png"
    BLACK_PAWN = "../img/black_pawn.png"
    BLACK_ROOK = "../img/black_rook.png"
    BLACK_KNIGHT = "../img/black_knight.png"
    BLACK_BISHOP = "../img/black_bishop.png"
    BLACK_QUEEN = "../img/black_queen.png"
    BLACK_KING = "../img/black_king.png"

DEFAULT_BOARD_IMAGES = {
        "A8": PieceImage.BLACK_ROOK.value,
        "B8": PieceImage.BLACK_KNIGHT.value,
        "C8": PieceImage.BLACK_BISHOP.value,
        "D8": PieceImage.BLACK_QUEEN.value,
        "E8": PieceImage.BLACK_KING.value,
        "F8": PieceImage.BLACK_BISHOP.value,
        "G8": PieceImage.BLACK_KNIGHT.value,
        "H8": PieceImage.BLACK_ROOK.value,
        "A7": PieceImage.BLACK_PAWN.value,
        "B7": PieceImage.BLACK_PAWN.value,
        "C7": PieceImage.BLACK_PAWN.value,
        "D7": PieceImage.BLACK_PAWN.value,
        "E7": PieceImage.BLACK_PAWN.value,
        "F7": PieceImage.BLACK_PAWN.value,
        "G7": PieceImage.BLACK_PAWN.value,
        "H7": PieceImage.BLACK_PAWN.value,
        "A2": PieceImage.WHITE_PAWN.value,
        "B2": PieceImage.WHITE_PAWN.value,
        "C2": PieceImage.WHITE_PAWN.value,
        "D2": PieceImage.WHITE_PAWN.value,
        "E2": PieceImage.WHITE_PAWN.value,
        "F2": PieceImage.WHITE_PAWN.value,
        "G2": PieceImage.WHITE_PAWN.value,
        "H2": PieceImage.WHITE_PAWN.value,
        "A1": PieceImage.WHITE_ROOK.value,
        "B1": PieceImage.WHITE_KNIGHT.value,
        "C1": PieceImage.WHITE_BISHOP.value,
        "D1": PieceImage.WHITE_QUEEN.value,
        "E1": PieceImage.WHITE_KING.value,
        "F1": PieceImage.WHITE_BISHOP.value,
        "G1": PieceImage.WHITE_KNIGHT.value,
        "H1": PieceImage.WHITE_ROOK.value,
    }


class Color(Enum):
    WHITE = "white"
    BLACK = "black"
    NOT_SET = ""

class LabelType(Enum):
    TILE = "board_tile_"
    STACK_PIECE = "stack_piece_"
    PIECE_COUNTER = "piece_counter_"