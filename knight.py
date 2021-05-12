from piece import Piece


class Knight(Piece):
    def __init__(self, row, col, player=1):
        super().__init__(row, col, player)
        self.char = 'C'
