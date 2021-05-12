
from rook import Rook
from knight import Knight
from bishop import Bishop
from pawn import Pawn

class ChessBoard():
    def __init__(self, name):
        self.name = name
        self.board = [
            [Rook(0,0), Knight(0,1), Bishop(0,2)],
            [Pawn(0,0), Pawn(0,1), Pawn(0,2)],
            [None, None,None,None,None, None,None,None],
        ]

    def draw(self):
        print('Chessboard: ', self.name)
        for row in range(3):
            for col in range(3):
                p = self.board[row][col]
                if p:
                    p.draw()

