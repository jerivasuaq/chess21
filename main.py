from chessboard import ChessBoard
from pawn import Pawn
from rook import Rook


print('Chess game')

chessb = ChessBoard('chessboard1')
chessb.draw()

valid = chessb.board[0][3].move(0,2)
print(valid)
valid = chessb.board[7][4].move(6,5)
print (valid)