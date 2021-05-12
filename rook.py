from piece import Piece


class Rook(Piece):
    def __init__(self, row, col, player=1):
        super().__init__(row, col, player)
        self.char = 'R'

