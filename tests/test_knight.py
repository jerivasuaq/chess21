import unittest
from knight import Knight
from pawn import Pawn
from test_utils import empty_board

class TestKnight(unittest.TestCase):
    def setUp(self):
        self.board = empty_board()
        self.knight = Knight(4, 4, 1)
        self.board.board[4][4] = self.knight

    def test_valid_moves(self):
        for (r, c) in [(6,5),(6,3),(2,5),(2,3),(5,6),(5,2),(3,6),(3,2)]:
            board = empty_board()
            k = Knight(4,4,1)
            board.board[4][4] = k
            self.assertTrue(k.move(r,c,board))

    def test_invalid_move(self):
        ok = self.knight.move(5,5,self.board)
        self.assertFalse(ok)

    def test_capture_enemy(self):
        self.board.board[6][5] = Pawn(6,5,2)
        ok = self.knight.move(6,5,self.board)
        self.assertTrue(ok)

    def test_blocked_ignores(self):
        # Knights should ignore blockers
        self.board.board[5][4] = Pawn(5,4,1)
        ok = self.knight.move(6,5,self.board)
        self.assertTrue(ok)

    def test_cannot_capture_ally(self):
        self.board.board[6][5] = Pawn(6,5,1)
        ok = self.knight.move(6,5,self.board)
        self.assertFalse(ok)

if __name__ == '__main__':
    unittest.main()
