import unittest
from rook import Rook
from pawn import Pawn
from test_utils import empty_board

class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = empty_board()
        self.rook = Rook(0, 0, 1)
        self.board.board[0][0] = self.rook

    def test_valid_move_horizontal(self):
        ok = self.rook.move(0, 5, self.board)
        self.assertTrue(ok)
        self.assertIs(self.board.board[0][5], self.rook)

    def test_blocked_path(self):
        self.board.board[0][3] = Pawn(0, 3, 1)
        ok = self.rook.move(0, 5, self.board)
        self.assertFalse(ok)
        self.assertIs(self.board.board[0][0], self.rook)

    def test_capture_enemy(self):
        self.board.board[0][5] = Pawn(0, 5, 2)
        ok = self.rook.move(0, 5, self.board)
        self.assertTrue(ok)
        self.assertIs(self.board.board[0][5], self.rook)

    def test_cannot_capture_ally(self):
        self.board.board[0][5] = Pawn(0, 5, 1)
        ok = self.rook.move(0, 5, self.board)
        self.assertFalse(ok)
        self.assertIs(self.board.board[0][0], self.rook)

    def test_invalid_diagonal(self):
        ok = self.rook.move(3, 3, self.board)
        self.assertFalse(ok)

if __name__ == '__main__':
    unittest.main()
