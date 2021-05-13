
from piece import Piece


class Queen(Piece):
    def __init__(self, row, col, player=1):
        super().__init__(row, col, player)
        self.char = 'Q'

    def move(self,drow,dcol):
        self.drow = drow
        self.dcol = dcol
        if (drow>7 or drow<0 or dcol>7 or dcol<0):
            return False
        elif (drow!=self.row and abs(drow-self.row)!=abs(dcol-self.col)) and (dcol!=self.col and abs(dcol-self.col)!=abs(drow-self.row)):
            return False
        else:
            return True
