from piece import Piece

class King(Piece):
    def __init__(self, row, col, player=1):
        super().__init__(row, col, player)
        self.char = 'K'
    
    def move(self,drow,dcol):
        self.drow = drow
        self.dcol = dcol
        if (drow>7 or drow<0 or dcol>7 or dcol<0):
            return False
        if drow >(self.row+1) or dcol>(self.col+1):
            return False
        elif drow <(self.row-1) or dcol<(self.col-1):
            return False
        else:
            return True