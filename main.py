from chessboard import ChessBoard
from bishop import Bishop
from king import King
from knight import Knight
from pawn import Pawn
from queen import Queen
from rook import Rook


print('Chess game')
board = ChessBoard('chessboard1')

P1 = Pawn(4,5,1)

B1 = Bishop(2,7,2)
B1.info()
board.board[2][7]=B1
board.board[4][5]=P1
board.draw()


B1.move(0,5,board)
B1.info()
board.draw()


B1.move(4,5,board)
B1.info()
board.draw()