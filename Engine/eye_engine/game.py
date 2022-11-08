
from typing import List, Optional, Tuple
from .engine import Engine
from .piece import Piece
from .player import Player
from .board import Board
from .position import Position


default_board: List[Tuple[Position, Piece.Type, Piece.Color]] = [
    (Position.from_name("a1"), Piece.Type.ROOK, Piece.Color.WHITE),
    (Position.from_name("b1"), Piece.Type.KNIGHT, Piece.Color.WHITE),
    (Position.from_name("c1"), Piece.Type.BISHOP, Piece.Color.WHITE),
    (Position.from_name("d1"), Piece.Type.QUEEN, Piece.Color.WHITE),
    (Position.from_name("e1"), Piece.Type.KING, Piece.Color.WHITE),
    (Position.from_name("f1"), Piece.Type.BISHOP, Piece.Color.WHITE),
    (Position.from_name("g1"), Piece.Type.KNIGHT, Piece.Color.WHITE),
    (Position.from_name("h1"), Piece.Type.ROOK, Piece.Color.WHITE),
    (Position.from_name("a2"), Piece.Type.PAWN, Piece.Color.WHITE),
    (Position.from_name("b2"), Piece.Type.PAWN, Piece.Color.WHITE),
    (Position.from_name("c2"), Piece.Type.PAWN, Piece.Color.WHITE),
    (Position.from_name("d2"), Piece.Type.PAWN, Piece.Color.WHITE),
    (Position.from_name("e2"), Piece.Type.PAWN, Piece.Color.WHITE),
    (Position.from_name("f2"), Piece.Type.PAWN, Piece.Color.WHITE),
    (Position.from_name("g2"), Piece.Type.PAWN, Piece.Color.WHITE),
    (Position.from_name("h2"), Piece.Type.PAWN, Piece.Color.WHITE),

    (Position.from_name("a8"), Piece.Type.ROOK, Piece.Color.BLACK),
    (Position.from_name("b8"), Piece.Type.KNIGHT, Piece.Color.BLACK),
    (Position.from_name("c8"), Piece.Type.BISHOP, Piece.Color.BLACK),
    (Position.from_name("d8"), Piece.Type.QUEEN, Piece.Color.BLACK),
    (Position.from_name("e8"), Piece.Type.KING, Piece.Color.BLACK),
    (Position.from_name("f8"), Piece.Type.BISHOP, Piece.Color.BLACK),
    (Position.from_name("g8"), Piece.Type.KNIGHT, Piece.Color.BLACK),
    (Position.from_name("h8"), Piece.Type.ROOK, Piece.Color.BLACK),
    (Position.from_name("a7"), Piece.Type.PAWN, Piece.Color.BLACK),
    (Position.from_name("b7"), Piece.Type.PAWN, Piece.Color.BLACK),
    (Position.from_name("c7"), Piece.Type.PAWN, Piece.Color.BLACK),
    (Position.from_name("d7"), Piece.Type.PAWN, Piece.Color.BLACK),
    (Position.from_name("e7"), Piece.Type.PAWN, Piece.Color.BLACK),
    (Position.from_name("f7"), Piece.Type.PAWN, Piece.Color.BLACK),
    (Position.from_name("g7"), Piece.Type.PAWN, Piece.Color.BLACK),
    (Position.from_name("h7"), Piece.Type.PAWN, Piece.Color.BLACK),
]


class Game:
    def __init__(self) -> None:
        self.board: Board = Board()
        self.white_player: Player = Player(Player.Color.WHITE)
        self.black_player: Player = Player(Player.Color.BLACK)
        self.current_player: Player = self.white_player
        self.winner: Optional[Player] = self.won()

        for position, piece_type, piece_color in default_board:
            self.board.add_piece(position, Piece(piece_type, piece_color))

    def switch_player(self):
        self.current_player = self.black_player if self.current_player.color is Player.Color.WHITE else self.white_player

    def won(self) -> Optional[Player]:
        return None

    def move(self, piece_position_name: str, target_position_name: str):
        piece_position = Position.from_name(piece_position_name)
        target_position = Position.from_name(target_position_name)
        Engine.move(piece_position, target_position, self.current_player.color, self.board)
        self.switch_player()

    def __str__(self):
        return f'\n{self.board}\n\n{str(self.winner) + " won!" if self.winner else str(self.current_player) + " to move"}'
