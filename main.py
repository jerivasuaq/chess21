from pawn import Pawn
from rook import Rook

print('Chess game')

p1 = Pawn(1, 1, 1)
p2 = Pawn(1, 2, 1)
p3 = Pawn(1, 3, 1)

p1.info()
p1.move(2,1)
p1.info()
p2.info()

r1 = Rook(0,1)
r2 = Rook(0,7)

r1.info()
