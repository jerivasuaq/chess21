
from bishop import Bishop
from king import King
from knight import Knight
from pawn import Pawn
from queen import Queen
from rook import Rook

class ChessBoard():
    def __init__(self, name):
        self.name = name
        # Initialize empty board
        self.board = [[None for _ in range(8)] for _ in range(8)]

        # Setup pieces
        def place_piece(piece_class, row, col, team):
            self.board[row][col] = piece_class(row, col, team)

        # Place main pieces for a team
        def setup_back_row(row, team):
            piece_order = [Rook, Knight, Bishop, Queen if row == 0 else King, 
                          King if row == 0 else Queen, Bishop, Knight, Rook]
            for col, piece_class in enumerate(piece_order):
                if piece_class in (King, Queen):
                    self.board[row][col] = piece_class(row, col, team)
                else:
                    self.board[row][col] = piece_class(row, col, team)

        # Place pawns
        def setup_pawns(row, team):
            for col in range(8):
                self.board[row][col] = Pawn(row, col, team)

        # Setup the board with all pieces
        setup_back_row(0, 1)  # Team 1 back row
        setup_pawns(1, 1)     # Team 1 pawns
        setup_pawns(6, 2)     # Team 2 pawns
        setup_back_row(7, 2)  # Team 2 back row

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
