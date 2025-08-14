import unittest
from queen import Queen
from pawn import Pawn
from test_utils import empty_board

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.board = empty_board()
        self.queen = Queen(4, 4, 1)
        self.board.board[4][4] = self.queen

    def test_valid_move_diagonal(self):
        ok = self.queen.move(1, 1, self.board)
        self.assertTrue(ok)
        self.assertIs(self.board.board[1][1], self.queen)

    def test_valid_move_straight(self):
        self.queen.move(4, 4, self.board)  # ensure position
        ok = self.queen.move(4, 7, self.board)
        self.assertTrue(ok)
        self.assertIs(self.board.board[4][7], self.queen)

    def test_blocked_path(self):
        self.board.board[4][6] = Pawn(4, 6, 1)
        ok = self.queen.move(4, 7, self.board)
        self.assertFalse(ok)

    def test_capture_enemy(self):
        self.board.board[1][1] = Pawn(1, 1, 2)
        ok = self.queen.move(1, 1, self.board)
        self.assertTrue(ok)

    def test_cannot_capture_ally(self):
        self.board.board[1][1] = Pawn(1, 1, 1)
        ok = self.queen.move(1, 1, self.board)
        self.assertFalse(ok)

    def test_invalid_move(self):
        ok = self.queen.move(6, 5, self.board)  # not straight or diagonal from (4,4)
        self.assertFalse(ok)

if __name__ == '__main__':
    unittest.main()
