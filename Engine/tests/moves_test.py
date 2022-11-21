import unittest
from eye_engine import Board, Piece
from eye_engine.position_constants import *  # pylint: disable=unused-wildcard-import, wildcard-import
from eye_engine.piece_constants import *  # pylint: disable=unused-wildcard-import, wildcard-import


class ValidMovesTest(unittest.TestCase):
    def test_knight_empty_board(self):
        self.assertEqual(Board([Piece(B2, KNIGHT, WHITE)]).valid_moves(B2), {A4, C4, D3, D1})

    def test_king_empty_board(self):
        self.assertEqual(Board([Piece(B2, KING, WHITE)]).valid_moves(B2), {C1, C2, C3, A1, A2, A3, B1, B3})

    def test_rook_empty_board(self):
        self.assertEqual(Board([Piece(D3, ROOK, WHITE)]).valid_moves(D3), {
                         D1, D2, D4, D5, D6, D7, D8, A3, B3, C3, E3, F3, G3, H3})

    def test_blocked_corner_rook(self):
        self.assertFalse(Board([Piece(A1, ROOK, WHITE), Piece(A2, PAWN, WHITE),
                         Piece(B1, KNIGHT, WHITE)]).valid_moves(A1))

    def test_capture_corner_rook(self):
        self.assertEqual(Board([Piece(A1, ROOK, WHITE), Piece(A2, PAWN, BLACK),
                         Piece(B1, KNIGHT, BLACK)]).valid_moves(A1), {A2, B1})

    def test_bishop_empty_board(self):
        self.assertEqual(Board([Piece(D4, BISHOP, WHITE)]).valid_moves(
            D4), {A1, B2, C3, E5, F6, G7, H8, G1, F2, E3, C5, B6, A7})

    def test_bishop_in_corner_empty_board(self):
        self.assertEqual(Board([Piece(H8, BISHOP, BLACK)]).valid_moves(H8), {A1, B2, C3, D4, E5, F6, G7})

    def test_queen_on_center_empty_board(self):
        self.assertEqual(Board([Piece(D4, QUEEN, WHITE)]).valid_moves(D4), {
                         A1, B2, C3, E5, F6, G7, H8, G1, F2, E3, C5, B6, A7, D1, D2, D3, D5, D6, D7, D8, A4, B4, C4, E4, F4, G4, H4})

    def test_only_white_pawn(self):
        self.assertEqual(Board([Piece(H2, PAWN, WHITE)]).valid_moves(H2), {H3, H4})

    def test_only_white_pawn_after_move(self):
        self.assertEqual(Board([Piece(A6, PAWN, WHITE)]).valid_moves(A6), {A7})

    def test_only_black_pawn(self):
        self.assertEqual(Board([Piece(H7, PAWN, BLACK)]).valid_moves(H7), {H6, H5})

    def test_only_black_pawn_after_move(self):
        self.assertEqual(Board([Piece(A5, PAWN, BLACK)]).valid_moves(A5), {A4})

    def test_black_pawn_capture(self):
        self.assertEqual(Board([Piece(A5, PAWN, BLACK), Piece(B4, PAWN, WHITE)]).valid_moves(A5), {A4, B4})

    def test_pawn_blocks_pawn(self):
        self.assertFalse(Board([Piece(A3, PAWN, WHITE), Piece(A4, PAWN, WHITE)]).valid_moves(A3))

    def test_all_valid_moves_default_board(self):
        self.assertEqual(Board.create_default().all_moves(), {A2: {A3, A4}, B1: {C3, A3}, G1: {H3, F3}, B2: {B3, B4},
                                                              C2: {C3, C4}, D2: {D3, D4}, E2: {E3, E4}, F2: {F3, F4},
                                                              G2: {G3, G4}, H2: {H3, H4}, A7: {A6, A5}, B7: {B6, B5},
                                                              C7: {C6, C5}, D7: {D6, D5}, E7: {E6, E5}, F7: {F6, F5},
                                                              G7: {G6, G5}, H7: {H6, H5}, B8: {A6, C6}, G8: {F6, H6}})


if __name__ == '__main__':
    unittest.main()
