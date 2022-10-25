from enum import Enum

TILE_SIZE = 60

DEFAULT_BOARD_IMAGES = {
        "A8": "../img/black_rook.png",
        "B8": "../img/black_knight.png",
        "C8": "../img/black_bishop.png",
        "D8": "../img/black_queen.png",
        "E8": "../img/black_king.png",
        "F8": "../img/black_bishop.png",
        "G8": "../img/black_knight.png",
        "H8": "../img/black_rook.png",
        "A7": "../img/black_pawn.png",
        "B7": "../img/black_pawn.png",
        "C7": "../img/black_pawn.png",
        "D7": "../img/black_pawn.png",
        "E7": "../img/black_pawn.png",
        "F7": "../img/black_pawn.png",
        "G7": "../img/black_pawn.png",
        "H7": "../img/black_pawn.png",
        "A2": "../img/white_pawn.png",
        "B2": "../img/white_pawn.png",
        "C2": "../img/white_pawn.png",
        "D2": "../img/white_pawn.png",
        "E2": "../img/white_pawn.png",
        "F2": "../img/white_pawn.png",
        "G2": "../img/white_pawn.png",
        "H2": "../img/white_pawn.png",
        "A1": "../img/white_rook.png",
        "B1": "../img/white_knight.png",
        "C1": "../img/white_bishop.png",
        "D1": "../img/white_queen.png",
        "E1": "../img/white_king.png",
        "F1": "../img/white_bishop.png",
        "G1": "../img/white_knight.png",
        "H1": "../img/white_rook.png",
    }

class Piece(Enum):
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


class Color(Enum):
    WHITE = "white"
    BLACK = "black"