
from piece import Piece


class Pawn(Piece):
    def __init__(self, row, col, player=1):
        super().__init__(row, col, player)
        self.char = 'P'

