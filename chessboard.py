
from bishop import Bishop
from king import King
from knight import Knight
from pawn import Pawn
from queen import Queen
from rook import Rook

class ChessBoard():
    def __init__(self, name):
        self.name = name
        self.board = [
            [Rook(0,0), Knight(0,1), Bishop(0,2),King(0,3),Queen(0,4),Bishop(0,5),Knight(0,6),Rook(0,7)],
            [Pawn(1,0), Pawn(1,1), Pawn(1,2),Pawn(1,3), Pawn(1,4), Pawn(1,5),Pawn(1,6),Pawn(1,7)],
            [None, None,None,None,None, None,None,None],
            [None, None,None,None,None, None,None,None],
            [None, None,None,None,None, None,None,None],
            [None, None,None,None,None, None,None,None],
            [Rook(7,0), Knight(7,1), Bishop(7,2),King(7,3),Queen(7,4),Bishop(7,5),Knight(7,6),Rook(7,7)],
            [Pawn(6,0), Pawn(6,1), Pawn(6,2),Pawn(6,3), Pawn(6,4), Pawn(6,5),Pawn(6,6),Pawn(6,7)],
        ]

    def draw(self):
        print('Chessboard: ', self.name)
        for row in range(8):
            for col in range(8):
                p = self.board[row][col]
                if p:
                    p.draw()
                else:
                    print('#' if(row+col%2 == 1) else ("*"), end='')
            print()

