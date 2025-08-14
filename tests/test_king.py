import unittest
from king import King
from pawn import Pawn
from test_utils import empty_board

class TestKing(unittest.TestCase):
    def setUp(self):
        self.board = empty_board()
        self.king = King(4, 4, 1)
        self.board.board[4][4] = self.king

    def test_valid_single_step(self):
        ok = self.king.move(5,5,self.board)
        self.assertTrue(ok)

    def test_invalid_far_move(self):
        ok = self.king.move(6,6,self.board)
        self.assertFalse(ok)

    def test_capture_enemy(self):
        self.board.board[5][5] = Pawn(5,5,2)
        ok = self.king.move(5,5,self.board)
        self.assertTrue(ok)

    def test_cannot_capture_ally(self):
        self.board.board[5][5] = Pawn(5,5,1)
        ok = self.king.move(5,5,self.board)
        self.assertFalse(ok)

if __name__ == '__main__':
    unittest.main()
