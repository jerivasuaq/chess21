
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
            [Rook(0,0,1), Knight(0,1,1), Bishop(0,2,1), King(0,3), Queen(0,4,1), Bishop(0,5,1), Knight(0,6,1), Rook(0,7,1)],
            [Pawn(1,0,1), Pawn(1,1,1), Pawn(1,2,1), Pawn(1,3,1), Pawn(1,4,1), Pawn(1,5,1), Pawn(1,6,1), Pawn(1,7,1)],
            [None, None,None,None,None, None,None,None],
            [None, None,None,None,None, None,None,None],
            [None, None,None,None,None, None,None,None],
            [None, None,None,None,None, None,None,None],
            [Pawn(6,0,2), Pawn(6,1,2), Pawn(6,2,2), Pawn(6,0,2), Pawn(6,1,2), Pawn(6,2,2), Pawn(6,0,2), Pawn(6,1,2)],
            [Rook(7,0,2), Knight(7,1,2), Bishop(7,2,2), King(7,3,2), Queen(7,4,2), Bishop(7,5,2), Knight(7,6,2), Rook(7,7,2)],
        ]

    def draw(self):
        print('Chessboard: ', self.name)
        for row in range(8):
            for col in range(8):
                p = self.board[row][col]
                if p:
                    print(' ', end='')
                    p.draw()
                    print(' |', end='')
                else:
                    print('████' if (row+col)%2 else '    ', end= '')
            print()
            for col in range(8):
                p = self.board[row][col]
                if p:
                    print('___|', end='')
                else:
                    print('████' if (row+col)%2 else '    ', end= '')
            print()

if __name__=='__main__':
    chessBoard = ChessBoard('chessboard1')
    chessBoard.draw()
