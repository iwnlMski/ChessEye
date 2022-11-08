import unittest
from eye_engine import Engine, Board, Position, Piece

WROOK = Piece(Piece.Type.ROOK, Piece.Color.WHITE)
BROOK = Piece(Piece.Type.ROOK, Piece.Color.BLACK)
WKNIGHT = Piece(Piece.Type.KNIGHT, Piece.Color.WHITE)
BKNIGHT = Piece(Piece.Type.KNIGHT, Piece.Color.BLACK)
WBISHOP = Piece(Piece.Type.BISHOP, Piece.Color.WHITE)
BBISHOP = Piece(Piece.Type.BISHOP, Piece.Color.BLACK)
WPAWN = Piece(Piece.Type.PAWN, Piece.Color.WHITE)
BPAWN = Piece(Piece.Type.PAWN, Piece.Color.BLACK)
WQUEEN = Piece(Piece.Type.QUEEN, Piece.Color.WHITE)
BQUEEN = Piece(Piece.Type.QUEEN, Piece.Color.BLACK)
WKING = Piece(Piece.Type.KING, Piece.Color.WHITE)
BKING = Piece(Piece.Type.KING, Piece.Color.BLACK)


class ValidMovesTest(unittest.TestCase):
    def validate_possible_moves(self, piece_position, pieces, expected_moves):
        board = Board()
        for position_str, piece in pieces:
            board.add_piece(Position.from_name(position_str), piece)
        self.assertCountEqual(Engine().valid_moves(Position.from_name(piece_position), board),
                              [Position.from_name(x) for x in expected_moves])

    def test_default_white_knight_valid_moves(self):
        self.validate_possible_moves("b2", [("b2", WKNIGHT)], ["a4", "c4", "d3", "d1"])

    def test_default_king_valid_moves(self):
        self.validate_possible_moves("b2", [("b2", WKING)], [
                                     "c1", "c2", "c3", "a1", "a2", "a3", "b1", "b3"])

    def test_default_rook_valid_moves(self):
        self.validate_possible_moves("d3", [("d3", WROOK)], ["d1", "d2", "d4", "d5", "d6", "d7", "d8",
                                                                         "a3", "b3", "c3", "e3", "f3", "g3", "h3"])

    def test_default_bishop_valid_moves(self):
        self.validate_possible_moves("d4", [("d4", WBISHOP)], ["a1", "b2", "c3", "e5", "f6", "g7", "h8",
                                                                           "g1", "f2", "e3", "c5", "b6", "a7"])

    def test_default_queen_valid_moves(self):
        self.validate_possible_moves("d4", [("d4", WQUEEN)], ["a1", "b2", "c3", "e5", "f6", "g7", "h8", "g1",
                                     "f2", "e3", "c5", "b6", "a7", "d1", "d2", "d3", "d5", "d6", "d7", "d8", "a4", "b4", "c4", "e4", "f4", "g4", "h4"])

    def test_corner_bishop_valid_moves(self):
        self.validate_possible_moves("h8", [("h8", BBISHOP)], ["a1", "b2", "c3", "d4", "e5", "f6", "g7"])

    def test_default_white_pawn_valid_moves(self):
        self.validate_possible_moves("h2", [("h2", WPAWN)], ["h3", "h4"])

    def test_white_pawn_after_move_valid_moves(self):
        self.validate_possible_moves("a6", [("a6", WPAWN)], ["a7"])

    def test_default_black_pawn_valid_moves(self):
        self.validate_possible_moves("h7", [("h7", BPAWN)], ["h6", "h5"])

    def test_black_pawn_after_move_valid_moves(self):
        self.validate_possible_moves("a5", [("a5", BPAWN)], ["a4"])


if __name__ == '__main__':
    unittest.main()
