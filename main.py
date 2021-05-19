from chessboard import ChessBoard
from pawn import Pawn
from rook import Rook


print('Chess game')

chessBoard = ChessBoard('chessboard1')
chessBoard.draw()

# valid = chessBoard.board[1][1].move(3, 1, chessBoard.board)
# print(valid)  # must be true
