from chessboard import ChessBoard
from pawn import Pawn
from rook import Rook


print('Chess game')

obj1 = ChessBoard('chessboard1')
obj1.draw()

p1 = Pawn(1, 1, 1)
p2 = Pawn(1, 2, 1)
p3 = Pawn(1, 3, 1)

r1 = Rook(0,1)
r2 = Rook(0,7)

p1.info()
r1.info()
