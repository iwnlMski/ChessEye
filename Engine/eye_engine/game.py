
from typing import Optional
from .piece import Piece
from .player import Player
from .board import Board
from .position import Position


class Game:
    def __init__(self) -> None:
        self.board: Board = Board.create_default()
        self.white_player: Player = Player(Piece.Color.WHITE)
        self.black_player: Player = Player(Piece.Color.BLACK)
        self.current_player: Player = self.white_player
        self.winner: Optional[Player] = self.won()

    def switch_player(self):
        self.current_player = self.black_player if self.current_player.owns_white() else self.white_player

    def won(self) -> Optional[Player]:
        # tested_color = Piece.Color.BLACK
        # other_color = Piece.Color.WHITE if tested_color == Piece.Color.BLACK else Piece.Color.BLACK

        # all_moves = Engine.valid_moves(self.board)
        # other_moves = [value for key, values in all_moves.items() for value in values if self.board.get_value(key).color
        # king_pos, king_moves = next(iter(king_moves_dict.items()))
        # opponent_moves = Engine.valid_moves(self.board, piece_color=other_color)

        # pass
        pass

    def move(self, piece_position_name: str, target_position_name: str):
        piece_position = Position(piece_position_name)
        target_position = Position(target_position_name)
        self.board.move(piece_position, target_position, self.current_player.piece_color)
        self.switch_player()

    def __str__(self):
        black_captures = "".join([str(p) for p in self.black_player.captured_pieces])
        white_captures = "".join([str(p) for p in self.white_player.captured_pieces])
        return f' {black_captures}\n{self.board}\n {white_captures}'

    def __repr__(self) -> str:
        return self.__str__()
