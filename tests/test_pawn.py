import unittest
from pawn import Pawn
from pawn import Piece
from test_utils import empty_board
from pawn import Pawn

class TestPawn(unittest.TestCase):
    def setUp(self):
        self.board = empty_board()
        self.pawn1 = Pawn(1, 3, 1)  # player 1 moves down (+1)
        self.board.board[1][3] = self.pawn1
        self.pawn2 = Pawn(6, 4, 2)  # player 2 moves up (-1)
        self.board.board[6][4] = self.pawn2

    def test_single_step(self):
        ok = self.pawn1.move(2,3,self.board)
        self.assertTrue(ok)

    def test_double_step_initial(self):
        ok = self.pawn1.move(3,3,self.board)
        self.assertTrue(ok)

    def test_double_step_blocked(self):
        # reset board
        self.board = empty_board()
        p = Pawn(1,0,1)
        self.board.board[1][0] = p
        blocker = Pawn(2,0,1)
        self.board.board[2][0] = blocker
        self.assertFalse(p.move(3,0,self.board))

    def test_capture(self):
        enemy = Pawn(2,4,2)
        self.board.board[2][4] = enemy
        ok = self.pawn1.move(2,4,self.board)
        self.assertTrue(ok)

    def test_invalid_capture_forward(self):
        ok = self.pawn1.move(2,3,self.board)  # forward move already tested
        self.assertTrue(ok)
        # try capturing forward (should fail)
        enemy = Pawn(3,3,2)
        self.board.board[3][3] = enemy
        self.assertFalse(self.pawn1.move(3,3,self.board))

    def test_player2_direction(self):
        ok = self.pawn2.move(5,4,self.board)
        self.assertTrue(ok)
        # invalid opposite direction
        self.assertFalse(self.pawn2.move(6,4,self.board))

if __name__ == '__main__':
    unittest.main()
