import unittest
from bishop import Bishop
from pawn import Pawn
from test_utils import empty_board

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.board = empty_board()
        self.bishop = Bishop(3, 3, 1)
        self.board.board[3][3] = self.bishop

    def test_valid_move_diagonal(self):
        ok = self.bishop.move(0, 0, self.board)
        self.assertTrue(ok)
        self.assertIs(self.board.board[0][0], self.bishop)

    def test_blocked_path(self):
        self.board.board[2][2] = Pawn(2, 2, 1)
        ok = self.bishop.move(0, 0, self.board)
        self.assertFalse(ok)
        self.assertIs(self.board.board[3][3], self.bishop)

    def test_capture_enemy(self):
        self.board.board[1][1] = Pawn(1, 1, 2)
        ok = self.bishop.move(1, 1, self.board)
        self.assertTrue(ok)
        self.assertIs(self.board.board[1][1], self.bishop)

    def test_cannot_capture_ally(self):
        self.board.board[1][1] = Pawn(1, 1, 1)
        ok = self.bishop.move(1, 1, self.board)
        self.assertFalse(ok)
        self.assertIs(self.board.board[3][3], self.bishop)

    def test_invalid_non_diagonal(self):
        ok = self.bishop.move(3, 5, self.board)
        self.assertFalse(ok)

if __name__ == '__main__':
    unittest.main()
